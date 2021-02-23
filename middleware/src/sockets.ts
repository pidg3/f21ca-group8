const fetch = require('node-fetch');
import WebSocket = require('ws');
import { v4 as uuidv4 } from 'uuid';

import { State, ExtWebSocket, MessageMetadata } from './types';

import { generateName } from './nameGenerator';
import { ChatLogger } from './chatLogger';

const ALANA_URL = 'http://52.56.181.83:5000';

const alanaBody = {
    'user_id': 'test-5827465823641856215',
    'session_id': 'Group8-Dev-1',
    'projectId': 'CA2020',
    'overrides': {}
};

const wss = new WebSocket.Server({
    port: 8080,
    clientTracking: true // needed for us to keep track of who is in the chat, nothing creepy
});

// Refactor: change metadata to just messageData, build the message in this function from
// its constituent parts
const broadcastMessage = (message: WebSocket.Data, metadata: MessageMetadata, sourceWs?: ExtWebSocket) => {
        
    wss.clients.forEach((client: any) => {
        // Only send to clients other than sourceWs (i.e. don't bounce user's
        // ... own messages back to them)
        if (sourceWs === undefined || client.id !== sourceWs.id) {
            client.send(message);
        } 
        
    })
};

function fetchData(appendedBody: object, data: string, metadata: MessageMetadata) {
    console.log(data);
    fetch(ALANA_URL, {
        method: 'POST',
        body: JSON.stringify({ ...appendedBody, question: data}),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then((res:any) => res.json())
                .then((json: any) => {
                    metadata.source = json.bot_name;              
                    broadcastMessage(`GLUE: ${json.result}`, metadata);
                })
}

//change to phase1Timer etc
var timer = 1;
var globalTimer = 1;
setTimeout(setGlobalTimer, 20000);

function setGlobalTimer() {
    globalTimer = -1000;
}

// Refactor: improve this state to use a proper singleton pattern
// (or at least give it a type)
export default (state: State) => {

    // Refactor: review all the logs in the whole codebase
    console.log('Sockets server set up on port 8080');
    
    wss.on('connection', (ws: ExtWebSocket, req) => {

        const id = uuidv4();
        const userName = generateName();
        console.log(`Connection established! ID: ${id}`);
        ws.id = id;
        ws.userName = userName;

        ws.send('~CONNECTED~'); // FE recognises this token

        ws.on('message', data => {
            console.log('data', data);

            const userMessageMetadata: MessageMetadata = {
                username: 'GLUE',
                glueBotUrl: state.externalBotUrl,
                designNumber: state.designNumber,
                tokens: '',
                source: ''
            };
            
            console.log(`Current external URL: ${state.externalBotUrl}`);
            broadcastMessage(`${ws.userName}: ${data}`, userMessageMetadata, ws);
            let appendedBody = { ...alanaBody };
            if (state.externalBotUrl !== '') {
                appendedBody.overrides = {
                    BOT_LIST: [{ glue: state.externalBotUrl}],
                    PRIORITY_BOTS: ['glue']
                };
            }

            clearTimeout(timer);

            const glueResponseMetadata: MessageMetadata = {
                username: 'GLUE',
                glueBotUrl: state.externalBotUrl,
                designNumber: state.designNumber,
                tokens: '',
                source: ''
            };

            if (globalTimer != -1000) {
                glueResponseMetadata.tokens = 'glue respond';
                fetchData(appendedBody, "glue respond " + data, glueResponseMetadata);
            } else if (data.toString().includes("GLUE")) {
                glueResponseMetadata.tokens = 'glue respond';
                fetchData(appendedBody, "glue respond " + data, glueResponseMetadata)
            } else {
                glueResponseMetadata.tokens = 'glue respond';
                timer = setTimeout(fetchData, 3000, appendedBody, "glue respond " + data);
            }
        });

        ws.on('close', function close() {
            ws.terminate();
            console.log(`Connection terminated: ID=${ws.id}`);
        });
    });
};
