import WebSocket = require('ws');

export interface State {
    externalBotUrl: string;
    alanaUUID: string;
    waitingForFirstMessage: boolean; // set to false as soon as first message received after a reset
    designNumber: number; // default

}

export interface ExtWebSocket extends WebSocket {
    id: string;
    userName: string;
}

export interface MessageMetadata {
    username: string;
    glueBotUrl: string;
    designNumber: number;
    tokens: string;
    source: string;
}