import { MessageData } from './types';
import { AppState } from './appState';

const DEFAULT_HISTORY_LIMIT = 200;

export class ChatLogger {
  private _appState: AppState;
  private _previousMessages: string[];
  private _historyLimit: number;

  // I.e. this class knows about the appState
  constructor(appState: AppState, historyLimit?: number) {
    this._previousMessages = [];
    this._appState = appState;
    this._historyLimit = historyLimit || DEFAULT_HISTORY_LIMIT;
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

  public logChatMessage(messageData: MessageData) {
    const formattedMessage = `EVAL_LOG: ${this.formatMessage(messageData)}`;
    this.appendToHistory(formattedMessage);
    console.log(formattedMessage);
  }

  public logDirect(message: string) {
    this.appendToHistory(message);
    console.log(message);
  }

  public getMessageHistory(limit: number) {
    if (limit > this._historyLimit) {
      return [`ERROR: can only request up to ${this._historyLimit} log messages`];
    }
    return this._previousMessages.slice(limit * -1);
  }

  private appendToHistory(message: string) {
    this._previousMessages.push(message);
    if (this._previousMessages.length > this._historyLimit) {
      this._previousMessages.shift();
    }
  }
}
