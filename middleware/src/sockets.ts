const fetch = require('node-fetch');
import WebSocket = require('ws');
import { v4 as uuidv4 } from 'uuid';

import { ExtWebSocket, MessageData } from './types';

import { AppState } from './app';

import { generateName } from './nameGenerator';

const ALANA_URL = 'http://52.56.181.83:5000';

const EXPRESS_URL = 'http://glue-middleware.eu-west-2.elasticbeanstalk.com';
// const EXPRESS_URL = ''; // nGrok URL here

const alanaBody = {
  user_id: 'test-5827465823641856215',
  projectId: 'CA2020',
  overrides: {}
};

const wss = new WebSocket.Server({
  port: 8080,
  clientTracking: true // needed for us to keep track of who is in the chat, nothing creepy
});

function messageContainsGreeting(message: string) {
  const lowerCaseMessage: string = message.toLowerCase();
  if (
    lowerCaseMessage.includes('hello') ||
    lowerCaseMessage.includes('hey') ||
    lowerCaseMessage.includes('hi') ||
    lowerCaseMessage.includes('yo') ||
    lowerCaseMessage.includes('ey up')
  ) {
    return true;
  }
  return false;
}

export default (appState: AppState) => {
  function fetchData(
    appendedBody: object,
    messageFromUser: string,
    tokens: string
  ) {
    // Append tokens if needed
    let alanaQuestion;
    if (tokens !== '') {
      alanaQuestion = `${tokens} ${messageFromUser}`;
    } else {
      alanaQuestion = messageFromUser;
    }

    console.log('Sent to Alana: ' + alanaQuestion);
    fetch(ALANA_URL, {
      method: 'POST',
      body: JSON.stringify({ ...appendedBody, question: alanaQuestion }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((res: any) => res.json())
      .then((json: any) => {
        broadcastMessage({
          message: json.result,
          source: json.bot_name,
          username: 'GLUE',
          tokens: tokens
        });
      });

    //whenever fetchData is called, clear the timer.
    clearTimeout(phase2Timer);
    phase2TimerFlag = false;
  }

  var phase2Timer: number;
  var greetingCounter = 0;
  var phase2TimerFlag = false;
  var previousMessage = '';
  var humanTokens: { [id: string]: string } = {};
  var previousHumanId = '';

  const broadcastMessage = (
    messageData: MessageData,
    sourceWs?: ExtWebSocket
  ) => {
    // Log for evaluation purposes
    appState.logger.logMessage(messageData);

    wss.clients.forEach((client: any) => {
      // Send all messages to admin clients, but in csv format
      if (client.type === 'admin') {
        client.send(appState.logger.formatMessage(messageData));
      } else {
        // For users...
        // only send to clients other than sourceWs (i.e. don't bounce user's
        // ... own messages back to them)
        if (sourceWs === undefined || client.id !== sourceWs.id) {
          client.send(`${messageData.username}: ${messageData.message}`);
        }
      }
    });
  };

  const newUserNotification = (username: string, sourceWs: ExtWebSocket) => {
    wss.clients.forEach((client: any) => {
      if (sourceWs === undefined || client.id !== sourceWs.id) {
        client.send(`New user ${username} joined the chat`);
      }
    });
  };

  // Refactor: review all the logs in the whole codebase
  console.log('Sockets server set up on port 8080');

  wss.on('connection', (ws: ExtWebSocket, req) => {
    const id = uuidv4();
    const username = generateName();
    ws.id = id;

    if (req !== undefined && req.url?.includes('type=admin')) {
      ws.type = 'admin';
    } else {
      ws.type = 'user';
      ws.username = username;
      ws.send(`~CONNECTED#${username}`); // FE recognises this token
      newUserNotification(username, ws);
      appState.addChatParticipant({
        id: id,
        username: username,
        joiningTime: new Date()
      });
    }

    console.log(
      `Connection established! Username=${ws.username || 'ADMIN'}, ID=${id}`
    );

    ws.on('message', data => {
      const message = data.toString();

      broadcastMessage(
        {
          message: message,
          source: 'USER',
          username: ws.username,
          tokens: ''
        },
        ws
      );

      let appendedBody = {
        ...alanaBody,
          session_id: appState.alanaSessionUUID
      };
      if (appState.externalBotUrl !== '') {
        appendedBody.overrides = {
          BOT_LIST: [{ glue: `${EXPRESS_URL}/glueProxy` }],
          PRIORITY_BOTS: ['glue']
        };
      }

      //this checks to see if a timer exists, if so, it'll look into "previousMessage" which stores the previous 'message'.
      //it then sends this with a glue keep quiet since we know the previous timer didn't hit 0.
      if (phase2TimerFlag == true) {
        const tokens = humanTokens[previousHumanId] + ' glue keep quiet';

        //console.log since GLUE isn't set up so Alana will respond to this currently.
        //console.log(humanTokens[ws.id] + " glue keep quiet " + previousMessage);
        fetchData(appendedBody, previousMessage, tokens);

        clearTimeout(phase2Timer);
        phase2TimerFlag = false;
      }

      //this is the new phase 1, we check if two "greeting" inputs are made before starting the GLUE talking session.
      if (greetingCounter < 2) {
        if (
          messageContainsGreeting(message) === true &&
          humanTokens[ws.id] == undefined
        ) {
          humanTokens[ws.id] = 'human_' + (greetingCounter + 1);
          const tokens = humanTokens[ws.id];
          fetchData(appendedBody, message, tokens);
          greetingCounter = greetingCounter + 1;
        }
      } else if (message.toLowerCase().includes('final answer is')) {
        const tokens = humanTokens[ws.id] + ' glue respond';
        fetchData(appendedBody, message, tokens);
      } else {
        //otherwise, wait 20 seconds and if no message appears, get GLUE response.
        //if a message is sent, reset this timer.
        const tokens = humanTokens[ws.id] + ' glue respond';
        previousMessage = message;
        phase2Timer = setTimeout(
          fetchData,
          20000,
          appendedBody,
          message,
          tokens
        );
        phase2TimerFlag = true;
        previousHumanId = ws.id;
      }
    });

    ws.on('close', function close() {
      ws.terminate();
      console.log(
        `Connection terminated! Username=${ws.username || 'ADMIN'}, ID=${ws.id}`
      );
    });
  });
};
