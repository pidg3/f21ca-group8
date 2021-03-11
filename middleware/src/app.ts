import expressApp from './express';
import socketsApp from './sockets';
import { AppState } from './appState';

// Note this will reset the Alana UUID and token state with each deploy
let appState = new AppState();

expressApp(appState);
socketsApp(appState);
