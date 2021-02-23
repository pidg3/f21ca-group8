import expressApp from './express';
import socketsApp from './sockets';
import { v4 as uuidv4 } from 'uuid';

import { State } from './types';

// Note this will reset the Alana UUID with each deploy
const starterAlanaUUID = uuidv4();
console.log(`Starter Alana UUID set: ${starterAlanaUUID}`);

enum Design {
    ChatbotOnly = 1,
    Gamification = 2
}

// This pattern is very nasty but will do for now...
let state: State = {
    externalBotUrl: '',
    alanaUUID: starterAlanaUUID,
    waitingForFirstMessage: true, // set to false as soon as first message received after a reset
    designNumber: Design.ChatbotOnly // default
};

expressApp(state);
socketsApp(state);