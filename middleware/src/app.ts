import expressApp from './express';
import socketsApp from './sockets';
import { v4 as uuidv4 } from 'uuid';

// Note this will reset the Alana UUID with each deploy

enum Design {
    ChatBot = 1,
    GameBot = 2
}

export class AppState {
    private _externalBotUrl: string;
    private _alanaUUID: string;
    private _waitingForFirstMessage: boolean;
    private _designNumber: number;

    constructor() {
        this._externalBotUrl = '';
        this._alanaUUID = uuidv4();
        this._waitingForFirstMessage = true; // set to false as soon as first message received after a reset
        this._designNumber = Design.ChatBot; // default

        console.log(`AppState initialised. Alana UUID: ${this._alanaUUID}`);
    }

    get externalBotUrl(): string {
        return this._externalBotUrl;
    }

    set externalBotUrl(newUrl: string) {
        // TODO: update logger when this changes
        // We want to both log out the change, and then use that new url for future
        // EVAL chat logs (same for designNumber)
        this._externalBotUrl = newUrl;
    }

    // TODO: is this worth logging out as well?
    get alanaUUID(): string {
        return this._alanaUUID;
    }

    get waitingForFirstMessage(): boolean {
        return this._waitingForFirstMessage;
    }

    public messageReceived() {
        this._waitingForFirstMessage = false;
    }

    get designNumber(): Design {
        return this._designNumber;
    }

    set designNumber(newDesign: Design) {
        // TODO: update logger
        this._designNumber = newDesign;
    }

    // Note - this doesn't change the external bot URL, or the design number
    public reset() {
        this._alanaUUID = uuidv4();
        this._waitingForFirstMessage = true;
        console.log(`AppState initialised. Alana UUID: ${this._alanaUUID}`);        
    }
}

let appState = new AppState();

expressApp(appState);
socketsApp(appState);