import WebSocket = require('ws');

export interface ExtWebSocket extends WebSocket {
    id: string;
    username: string;
    type: string;
}

export interface MessageData {
    message: string;
    username: string;
    tokens: string;
    source: string;
}

export interface ChatParticipant {
    username: string;
    id: string;
    joiningTime: Date;
}