import expressApp from './express';
import socketsApp from './sockets';
import { v4 as uuidv4 } from 'uuid';

import { ChatLogger } from './chatLogger';

import { ChatParticipant, TokenControl } from './types';

// Note this will reset the Alana UUID with each deploy

enum Design {
  ChatBot = 1,
  GameBot = 2
}

export class AppState {
  public logger: ChatLogger;

  private _externalBotUrl: string;
  private _alanaSessionUUID: string;
  private _designNumber: number;
  private _chatParticipants: ChatParticipant[];

  constructor() {
    this.logger = new ChatLogger(this);
    this._externalBotUrl = '';
    this._alanaSessionUUID = uuidv4();
    this._designNumber = Design.ChatBot; // default
    this._chatParticipants = [];

    console.log(`AppState initialised. Alana UUID: ${this._alanaSessionUUID}`);
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
  get alanaSessionUUID(): string {
    return this._alanaSessionUUID;
  }

  get designNumber(): Design {
    return this._designNumber;
  }

  set designNumber(newDesign: Design) {
    // TODO: update logger
    this._designNumber = newDesign;
  }

  get chatParticipants(): ChatParticipant[] {
    return this._chatParticipants;
  }

  public addChatParticipant(newJoiner: ChatParticipant): void {
    this._chatParticipants.push(newJoiner);
  }

  public removeChatParticipant(idToRemove: string) {
    return this._chatParticipants.find(cp => cp.id === idToRemove);
  }

  // Note - this doesn't change the external bot URL, or the design number
  public reset(): void {
    this._alanaSessionUUID = uuidv4();
    console.log(`AppState initialised. Alana UUID: ${this._alanaSessionUUID}`);
  }
}

let appState = new AppState();

expressApp(appState);
socketsApp(appState);
