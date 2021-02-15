const fetch = require('node-fetch');
import WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

const alanaBody = {
    'user_id': 'test-5827465823641856215',
    'session_id': 'Group8-Dev-1',
    'projectId': 'CA2020'
};

export default () => {
    console.log('Sockets server set up on ws://localhost:8080');
    
    wss.on('connection', ws => {
        console.log('Connection established!');
        ws.send('Established connection');

        ws.on('message', data => {
            console.log(`Received message: ${data}`);
            fetch('http://52.56.181.83:5000', {
                method: 'POST',
                body: JSON.stringify({...alanaBody, question: data}),
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
            console.log('Connection terminated');

        });
    });
};