import expressApp from './express';
import socketsApp from './sockets';

// This pattern is very nasty but will do for now...
let state = {
    externalBotUrl: ''
};

expressApp(state);
socketsApp(state);