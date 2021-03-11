import express from 'express';
import cors from 'cors';
import { AppState } from './appState';
const fetch = require('node-fetch');

const app = express();

// Remember, this is defined manually as an env variable in EB
// (which overrides the confusing, default/hidden 8080 value, which is
// ... reserved for web socket)
const PORT = process.env.PORT || 8090;

const start = (appState: AppState) => {
  app.use(cors());
  app.use(express.json({ limit: '5mb' }));

  app.get('/', (req: any, res: any) => res.send('OK!'));

  app.get('/chatParticipants', (req: any, res: any) => {
    res.send(appState.chatParticipants);
  });

  app.get('/externalBotUrl', (req: any, res: any) => {
    let response: string;
    if (appState.externalBotUrl === '') {
      response = 'Glue bot URL not defined - using vanilla Alana only\n';
    } else {
      response = appState.externalBotUrl + '\n';
    }
    res.send(response);
  });

  app.post('/setExternalBotUrl', (req: any, res: any) => {
    if (req.body.externalBotUrl === '') {
      appState.externalBotUrl = '';
    } else {
      appState.externalBotUrl = `${req.body.externalBotUrl}/webhooks/rest/webhook`;
    }
    res.send('Success! External bot URL set\n');
  });

  app.post('/resetState', (req: any, res: any) => {
    appState.reset();
    res.send('Success! State reset\n');
  });

  app.get('/logs', (req: any, res: any) => {
    const logs = appState.logger.getMessageHistory(req.query.limit).join('\n') + '\n';
    res.send(logs);
  });

  app.post('/glueProxy', (req: any, res: any) => {
    appState.logger.logDirect('--- Glue Proxy Invoked ---');
    const userMessage = req.body.current_state.state.input.text;

    // Call the RASA bot
    fetch(appState.externalBotUrl, {
      method: 'POST',
      body: JSON.stringify({
        sender: 'test_user',
        message: userMessage
      }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then((res: any) => res.json())
      .then((json: any) => {
        appState.logger.logDirect('RASA Response:' + JSON.stringify(json));
        const result = {
          result: json[0].text,
          bot_name: 'glue',
          lock_requested: false,
          bot_params: {
            something: 1
          }
        };

        res.json([result]);
      })
      .catch((err: Error) => {
        appState.logger.logDirect(err.message);
        res.json([]);
      });
  });

  app.listen(PORT, () => {
    appState.logger.logDirect(`⚡️[server]: Server is running at port ${PORT}`);
  });
};

export default start;
