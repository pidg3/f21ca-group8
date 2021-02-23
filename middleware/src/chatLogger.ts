import { MessageData } from './types';

// TODO: write some tests for this - make sure quote escaping working properly
export class ChatLogger {

    static escapeQuotes(message: string) {
        // TODO: escape quotes (i.e. user enters " in message")
        return message;
    }

    static logMessage(messageData: MessageData) {

        const ts = new Date();
        const quoteEscapedMessage = this.escapeQuotes(messageData.message);
        console.log(

            // Add an identifier so these can be easily spotted/extracted from the logs
            'EVAL_LOG: ' +

            // Timestamp
            `${ts.getFullYear()}-${ts.getMonth() + 1}-${ts.getDate()}T` +
            `${ts.getHours()}:${ts.getMinutes()}:${ts.getSeconds()}:${ts.getMilliseconds()}Z,` +

            // Glue bot url (note, may be empty string)
            // `${messageData.glueBotUrl},` + TODO: change to state

            `${messageData.username},` +
            // `${messageData.designNumber},` + // TODO: change to state

            // Note we wrap message in quotes in case user/bot has entered a comma
            `"${quoteEscapedMessage}",` +

            `${messageData.tokens},` +
            `${messageData.source}`
        );
    }
}