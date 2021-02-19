import expressApp from './express';
import socketsApp from './sockets';
import { v4 as uuidv4 } from 'uuid';

// Note this will reset the Alana UUID with each deploy
const starterAlanaUUID = uuidv4();
console.log(`Starter Alana UUID set: ${starterAlanaUUID}`);

// This pattern is very nasty but will do for now...
let state = {
    externalBotUrl: '',
    alanaUUID: starterAlanaUUID,
    waitingForFirstMessage: true // set to false as soon as first message received after a reset
};

expressApp(state);
socketsApp(state);