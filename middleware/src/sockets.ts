const fetch = require('node-fetch');
import WebSocket = require('ws');

const alanaBody = {
    'user_id': 'test-5827465823641856215',
    'session_id': 'Group8-Dev-1',
    'projectId': 'CA2020',
    'overrides': {}
};

const wss = new WebSocket.Server({ port: 8080 });

export default (state:any) => {


    console.log('Sockets server set up on ws://localhost:8080');
    
    wss.on('connection', ws => {

        console.log('Connection established!');
        ws.send('~CONNECTED~');

        ws.on('message', data => {
            console.log(`Current external URL: ${state.externalBotUrl}`);
            
            let appendedBody = { ...alanaBody };
            if (state.externalBotUrl !== '') {
                appendedBody.overrides = {
                    BOT_LIST: [{ glue: state.externalBotUrl}],
                    PRIORITY_BOTS: ['glue']
                };
            }
            console.log(`Received message: ${data}`);
            fetch('http://52.56.181.83:5000', {
                method: 'POST',
                body: JSON.stringify({ ...appendedBody, question: data}),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then((res:any) => res.json())
                .then((json: any) => {
                    console.log(json);
                    
                    ws.send(json.result);
                })
        });

        ws.on('close', function close() {
            ws.terminate();
            console.log('Connection terminated');
        });
    });
};