import { v4 as uuidv4 } from 'uuid';

import { ChatLogger } from './chatLogger';
import { ChatParticipant, TokenControl } from './types';

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
  private _phase2Timer: number;
  private _greetingCounter: number;
  private _phase2TimerFlag: boolean;
  private _previousMessage: string;
  private _humanTokens: { [id: string]: string };
  private _previousHumanId: string;


  constructor() {
    this.logger = new ChatLogger(this);
    this._externalBotUrl = '';
    this._alanaSessionUUID = uuidv4();
    this._designNumber = Design.ChatBot; // default
    this._chatParticipants = [];
    this._greetingCounter = 1;
    this._phase2TimerFlag = false;
    this._previousMessage = '';
    this._humanTokens = {};
    this._previousHumanId = '';

    this.logger.logDirect(`AppState initialised. Alana UUID: ${this._alanaSessionUUID}`);
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

  get greetingCounter() {
    return this._greetingCounter;
  }

  set phase2Timer(timer: number) {
    this._phase2Timer = timer;
  }

  public cancelPhase2Timer() {
    clearTimeout(this._phase2Timer);
  }


  get phase2TimerFlag(): boolean {
    return this._phase2TimerFlag;
  }

  set phase2TimerFlag(value: boolean) {
    this._phase2TimerFlag = value;
  }

  get previousMessage(): string {
    return this._previousMessage;
  }

  set previousMessage(value: string) {
    this._previousMessage = value;
  }

  public getHumanTokenFromId(id: string) {
    return (this._humanTokens[id]);
  }

  public appendHumanToken(id: string) {
    this._humanTokens[id] = `human_${this._greetingCounter}`;
    this._greetingCounter += 1;
  }

  get previousHumanId(): string {
    return this._previousHumanId;
  }

  set previousHumanId(value: string) {
    this._previousHumanId = value;
  }

  // Note - this doesn't change the external bot URL, or the design number
  public reset(): void {
    this._alanaSessionUUID = uuidv4();
    this._chatParticipants = [];
    this._greetingCounter = 1;
    this._phase2TimerFlag = false;
    this._previousMessage = '';
    this._humanTokens = {};
    this._previousHumanId = '';

    this.logger.logDirect(`AppState initialised. Alana UUID: ${this._alanaSessionUUID}`);
  }
}
