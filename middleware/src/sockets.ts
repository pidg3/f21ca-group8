const fetch = require('node-fetch');
import WebSocket = require('ws');
import { v4 as uuidv4 } from 'uuid';

import { ExtWebSocket, MessageData } from './types';

import { AppState } from './appState';

import { generateName } from './nameGenerator';

const ALANA_URL = 'http://52.56.181.83:5000';

const EXPRESS_URL = 'http://glue-middleware.eu-west-2.elasticbeanstalk.com';

const SILENT_RESPONSE_TOKEN = 'silent_response';

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
    lowerCaseMessage.includes('hi') ||
    lowerCaseMessage.includes('hiya') ||
    lowerCaseMessage.includes('holla')
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
      // Note double space between tokens and message, as per instructions
      alanaQuestion = `${tokens}  ${messageFromUser}`;
    } else {
      alanaQuestion = messageFromUser;
    }

    console.log(alanaQuestion);

    appState.logger.logDirect('Sent to Alana: ' + alanaQuestion);
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
    clearTimeout(appState.phase2Timer);
    appState.phase2TimerFlag = false;
  }

  const broadcastMessage = (
    messageData: MessageData,
    sourceWs?: ExtWebSocket
  ) => {
    // Log for evaluation purposes
    appState.logger.logChatMessage(messageData);

    wss.clients.forEach((client: any) => {
      // Send all messages to admin clients, but in csv format
      if (client.type === 'admin') {
        client.send(appState.logger.formatMessage(messageData));
      } else if (messageData.message !== SILENT_RESPONSE_TOKEN) {
        // For users, we only send the message if the message is not our silent response token,
        // ... AND the user is not the one sending the message
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

  appState.logger.logDirect('Sockets server set up on port 8080');

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

    appState.logger.logDirect(
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
          BOT_LIST: [{ glue: `${EXPRESS_URL}/glueProxy` }, ...appState.alanaBots],
          PRIORITY_BOTS: ['glue', ...appState.alanaBots]
        };
      }

      appState.logger.logDirect(`appendedBody: ${JSON.stringify(appendedBody)}`);

      //this checks to see if a timer exists, if so, it'll look into "previousMessage" which stores the previous 'message'.
      //it then sends this with a glue keep quiet since we know the previous timer didn't hit 0.
      if (appState.phase2TimerFlag == true) {
        const humanNumber = appState.getHumanTokenFromId(appState.previousHumanId);
        const tokens = `${humanNumber} glue keep quiet`;

        fetchData(appendedBody, appState.previousMessage, tokens);

        appState.cancelPhase2Timer();
        appState.phase2TimerFlag = false;
      }

      var filteredMessage = message.toLowerCase().split(' glue ').join(" ");
      filteredMessage = filteredMessage.split(' glue').join("");
      filteredMessage = filteredMessage.split('glue ').join("");
      filteredMessage = filteredMessage.split('\bglue\b').join(" ");

      //this is the new phase 1, we check if two "greeting" inputs are made before starting the GLUE talking session.
      if (appState.greetingCounter <= 2) {
        if (
          messageContainsGreeting(filteredMessage) === true &&
          appState.getHumanTokenFromId(ws.id) == undefined
        ) {
          appState.appendHumanToken(ws.id);
          const tokens = appState.getHumanTokenFromId(ws.id);
          fetchData(appendedBody, filteredMessage, tokens);
        }
      } else if (filteredMessage.toLowerCase().includes('final answer is')) {
        const humanNumber = appState.getHumanTokenFromId(ws.id);
        const tokens = `${humanNumber} glue respond`;
        fetchData(appendedBody, filteredMessage, tokens);
      } else {
        //otherwise, wait 20 seconds and if no message appears, get GLUE response.
        //if a message is sent, reset this timer.
        const humanNumber = appState.getHumanTokenFromId(ws.id);
        const tokens = `${humanNumber} glue respond`;
        appState.previousMessage = filteredMessage;
        appState.phase2Timer = setTimeout(
          fetchData,
          20000,
          appendedBody,
          filteredMessage,
          tokens
        );
        appState.phase2TimerFlag = true;
        appState.previousHumanId = ws.id;
      }
    });

    ws.on('close', function close() {
      ws.terminate();
      appState.logger.logDirect(
        `Connection terminated! Username=${ws.username || 'ADMIN'}, ID=${ws.id}`
      );
    });
  });
};
