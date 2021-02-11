// https://flaviocopes.com/node-websockets/
const fetch = require('node-fetch');
import WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 })

export default () => {
    console.log('Sockets server set up on ws://localhost:8080');
    
    wss.on('connection', ws => {
        console.log('Connection established!');
        ws.send('Established connection');

        ws.on('message', data => {
            console.log(`Received message: ${data}`);
            fetch('https://icanhazdadjoke.com/', {
                headers: {
                    'accept': 'application/json'
                }
            })
                .then((res:any) => res.json())
                .then((json:any) => {
                    ws.send(`Thanks for the message: ${data}`)
                    ws.send(`Here is a joke: ${json.joke}`)

                });
            
        });

        ws.on('close', function close() {
            console.log('Connection terminated');

        });
    });
};