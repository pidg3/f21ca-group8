import { MessageData } from './types';
import { AppState } from './app';

// TODO: write some tests for this - make sure quote escaping working properly
export class ChatLogger {

    private _appState: AppState;

    // I.e. this class knows about the appState
    constructor(appState: AppState) {
        this._appState = appState;
    }

    private escapeQuotes(message: string) {
        // TODO: escape quotes (i.e. user enters " in message")
        return message;
    }

    // We expose this publicly as we call it in the admin view
    public formatMessage(messageData: MessageData) {
        const ts = new Date();
        const quoteEscapedMessage = this.escapeQuotes(messageData.message);
        // The ordering of this is a bit weird, kept the same as I put on Teams
        // ... to avoid confusion
        return (

            // Timestamp
            `${ts.getFullYear()}-${ts.getMonth() + 1}-${ts.getDate()}T` +
            `${ts.getHours()}:${ts.getMinutes()}:${ts.getSeconds()}.${ts.getMilliseconds()}Z,` +

            // Glue bot url (note, may be empty string)
            `${this._appState.externalBotUrl},` +

            `${messageData.username},` +
            `${this._appState.designNumber},` +

            // Note we wrap message in quotes in case user/bot has entered a comma
            `"${quoteEscapedMessage}",` +

            `${messageData.tokens},` +
            `${messageData.source}`
        );
    }

    public logMessage(messageData: MessageData) {
        console.log('EVAL_LOG: ' + this.formatMessage(messageData));
    }
}