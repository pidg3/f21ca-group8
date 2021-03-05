const fetch = require('node-fetch');
import WebSocket = require('ws');
import { v4 as uuidv4 } from 'uuid';

import { ExtWebSocket, MessageData } from './types';

import { AppState } from './app';

import { generateName } from './nameGenerator';

const ALANA_URL = 'http://52.56.181.83:5000';

const EXPRESS_URL = 'http://glue-middleware.eu-west-2.elasticbeanstalk.com';
// const EXPRESS_URL = 'http://f1f7ec8d1202.ngrok.io';

const alanaBody = {
    'user_id': 'test-5827465823641856215',
    'session_id': 'Group8-Dev-2',
    'projectId': 'CA2020',
    'overrides': {}
};

const wss = new WebSocket.Server({
    port: 8080,
    clientTracking: true // needed for us to keep track of who is in the chat, nothing creepy
});

export default (appState: AppState) => {

    function fetchData(appendedBody: object, messageFromUser: string, tokens: string) {

        // Append tokens if needed
        let alanaQuestion;
        if (tokens !== '') {
            alanaQuestion = `${tokens} ${messageFromUser}`;
        } else {
            alanaQuestion = messageFromUser;
        }

        fetch(ALANA_URL, {
            method: 'POST',
            body: JSON.stringify({ ...appendedBody, question: alanaQuestion }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then((res: any) => res.json())
            .then((json: any) => {
                broadcastMessage({
                    message: json.result,
                    source: json.bot_name,
                    username: 'GLUE',
                    tokens: tokens
                });
            })

        //whenever fetchData is called, clear the timer.
        clearTimeout(phase2Timer);
        phase2TimerFlag = false;
    }

    //change to phase1Timer etc
    var phase2Timer = 1;
    var helloCounter = 0;
    var phase2TimerFlag = false;
    var msg = "";

    const broadcastMessage = (messageData: MessageData, sourceWs?: ExtWebSocket) => {

        // Log for evaluation purposes
        appState.logger.logMessage(messageData);

        wss.clients.forEach((client: any) => {

            // Send all messages to admin clients, but in csv format
            if (client.type === 'admin') {
                client.send(appState.logger.formatMessage(messageData));
            }

            else {
                // For users...
                // only send to clients other than sourceWs (i.e. don't bounce user's
                // ... own messages back to them)
                if (sourceWs === undefined || client.id !== sourceWs.id) {
                    client.send(`${messageData.username}: ${messageData.message}`);
                }

            }

        });
    };

    const newUserNotification = (username: string, sourceWs: ExtWebSocket) => {
        wss.clients.forEach((client: any) => {
            if (sourceWs === undefined || client.id !== sourceWs.id) {
                client.send(`New user ${username} joined the chat`);
            }
        });

    }

    // Refactor: review all the logs in the whole codebase
    console.log('Sockets server set up on port 8080');
    
    wss.on('connection', (ws: ExtWebSocket, req) => {
    
        const id = uuidv4();
        const username = generateName();
        ws.id = id;

        if (req !== undefined && req.url?.includes('type=admin')) {
            ws.type = 'admin';
        } else {
            ws.type = 'user';
            ws.username = username;
            ws.send(`~CONNECTED#${username}`); // FE recognises this token
            newUserNotification(username, ws);
            appState.addChatParticipant({
                id: id,
                username: username,
                joiningTime: new Date()
            })
        }

        console.log(`Connection established! Username=${ws.username || 'ADMIN'}, ID=${id}`);

        

        ws.on('message', data => {

            const message = data.toString();
            console.log('data', data);
            
            broadcastMessage({
                message: message,
                source: 'USER',
                username: ws.username,
                tokens: ''
            }, ws);

            let appendedBody = { ...alanaBody };
            if (appState.externalBotUrl !== '') {
                appendedBody.overrides = {
                    BOT_LIST: [{ glue: `${EXPRESS_URL}/glueProxy`}],
                    PRIORITY_BOTS: ['glue']
                };
            }
        

            //this checks to see if a timer exists, if so, it'll look into "msg" which stores the previous msg.
            //it then sends this with a glue keep quiet since we know the previous timer didn't hit 0.
            if (phase2TimerFlag == true) {
                const tokens = 'glue keep quiet';

                // console.log since GLUE isn't set up so Alana will respond to this currently.
                console.log("glue keep quiet " + msg);
                //fetchData(appendedBody, msg, tokens);

                clearTimeout(phase2Timer);
                phase2TimerFlag = false;
            }


            //this is the new phase 1, we check if two "Hello" inputs are made before starting the GLUE talking session.
            if (helloCounter != 2) {
                if (message == "Hello") {
                    if (helloCounter == 1) {
                        const tokens = 'glue respond';
                        fetchData(appendedBody, message, tokens);
                    }
    
                    helloCounter = helloCounter + 1;
                }
            } else if (data.toString().includes("GLUE")) {
                //If GLUE is mentioned, we get GLUE to respond instantly
                const tokens = 'glue respond';
                fetchData(appendedBody, message, tokens);
            } else {
                //otherwise, wait 20 seconds and if no message appears, get GLUE response.
                //if a message is sent, reset this timer.
                const tokens = 'glue respond';
                msg = message;
                phase2Timer = setTimeout(fetchData, 20000, appendedBody, message, tokens);
                phase2TimerFlag = true;
            }
        });

        ws.on('close', function close() {
            ws.terminate();
            console.log(`Connection terminated! Username=${ws.username || 'ADMIN'}, ID=${ws.id}`);
        });
    });
};
