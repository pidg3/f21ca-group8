import WebSocket = require('ws');

export interface ExtWebSocket extends WebSocket {
    id: string;
    userName: string;
}

export interface MessageData {
    message: string;
    username: string;
    tokens: string;
    source: string;
}