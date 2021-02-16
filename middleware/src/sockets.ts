const fetch = require('node-fetch');
import WebSocket = require('ws');
import { v4 as uuidv4 } from 'uuid';

import nameGenerator from './nameGenerator';

const ALANA_URL = 'http://52.56.181.83:5000';

interface ExtWebSocket extends WebSocket {
    id: string;
    userName: string;
}

const alanaBody = {
    'user_id': 'test-5827465823641856215',
    'session_id': 'Group8-Dev-1',
    'projectId': 'CA2020',
    'overrides': {}
};

const wss = new WebSocket.Server({
    port: 8080,
    clientTracking: true
});

const broadcastMessage = (message: WebSocket.Data, sourceWs?: ExtWebSocket) => {
    
    wss.clients.forEach((client: any) => {
        // Only send to clients other than sourceWs (i.e. don't bounce user's
        // ... own messages back to them)
        if (sourceWs === undefined || client.id !== sourceWs.id) {
            client.send(message);
        } 
        
    })
};

export default (state:any) => {


    console.log('Sockets server set up on port 8080');
    
    wss.on('connection', (ws: ExtWebSocket, req) => {

        const id = uuidv4();
        const userName = nameGenerator();
        console.log(`Connection established! ID: ${id}`);
        ws.id = id;
        ws.userName = userName;

        ws.send('~CONNECTED~'); // FE recognises this token

        ws.on('message', data => {
            console.log('data', data);
            
            console.log(`Current external URL: ${state.externalBotUrl}`);
            broadcastMessage(`${ws.userName}: ${data}`, ws);
            let appendedBody = { ...alanaBody };
            if (state.externalBotUrl !== '') {
                appendedBody.overrides = {
                    BOT_LIST: [{ glue: state.externalBotUrl}],
                    PRIORITY_BOTS: ['glue']
                };
            }
            fetch(ALANA_URL, {
                method: 'POST',
                body: JSON.stringify({ ...appendedBody, question: data}),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then((res:any) => res.json())
                .then((json: any) => {                    
                    broadcastMessage(`Alana: ${json.result}`);
                })
        });

        ws.on('close', function close() {
            ws.terminate();
            console.log(`Connection terminated: ID=${ws.id}`);
        });
    });
};