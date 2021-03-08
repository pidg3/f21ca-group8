# F21CA - Group 8

This is a monorepo containing the three parts of our code:

- `gui/`: front end, basic chat window. Hosted here: http://glue-bot.s3-website.eu-west-2.amazonaws.com/. Deploys automatically to S3 with a push to `master`. 
- `middleware/`: node service providing basic message forwarding for multi-party chat, issuing of requests to Alana/GLUE, and logging of statistics for evaluation. Hosted here: http://glue-middleware.eu-west-2.elasticbeanstalk.com. Requires manual deployment to Elastic Beanstalk.
- `rasa/`: Python code implementing our GLUE bot (note, this will be accessed as an Alana bot). Requires hosting via nGrok or similar tool, and the URL passing into the GUI. 

For local development, you need to swap over the `EXPRESS_URL` and `SOCKETS_URL` values at the top of `gui/src/UserView.js` and `gui/src/AdminView.js`. This will point the gui at your local express server, rather than the one hosted on AWS.

## How to debug the tokens/RASA locally

Note that only one instance is currently hosted, so we might need to coordinate as if two groups are trying to do this at the same time, the URLs will get into a muddle.

This is missing the functionality for resetting the chat state: it won't work properly until this is done, however it should allow you to test your connection to the GLUE bot. 

1. Spin up your RASA bot. Note the port it is exposed on (this is normally localhost:5005).
2. Expose the RASA bot via nGrok: `ngrok http [rasa port]`, i.e. `ngrok http 5005` if the port follows the above pattern.
3. Tell the app what the ngrok URL for the GLUE bot is via cUrl: `curl -X POST --header "Content-Type: application/json" --data '{"externalBotUrl":"[URL]"}' http://glue-middleware.eu-west-2.elasticbeanstalk.com/setExternalBotUrl`
4. Check this has worked properly: `curl http://glue-middleware.eu-west-2.elasticbeanstalk.com/externalBotUrl` should return the URL with an extra bit at the end: 'webhooks/rest/webhook'.
5. Go to the usual URL in the browser: http://glue-bot.s3-website.eu-west-2.amazonaws.com/
6. Open up the admin views in separate tabs: http://glue-bot.s3-website.eu-west-2.amazonaws.com/readable and http://glue-bot.s3-website.eu-west-2.amazonaws.com/admin
7. Press the 'Connect' button (in multiple tabs if needed). 
8. When the chat has finshed, remember to copy out the logs from the admin view and paste into a spreadsheet for evaluation purposes. 

## Curl commands

If you need to run these on your local middleware build, replace `glue-middleware.eu-west-2.elasticbeanstalk.com` with `localhost:8090`.

- Reset bot state (resets Alana session ID and timers, but **NOT** the design (`ChatBot/GameBot`) or the GLUE bot URL): `curl -X POST http://glue-middleware.eu-west-2.elasticbeanstalk.com/resetState`
- Update GLUE bot URL: `curl -X POST --header "Content-Type: application/json" --data '{"externalBotUrl":"[URL]"}' http://glue-middleware.eu-west-2.elasticbeanstalk.com/setExternalBotUrl`
- Get current GLUE bot URL: `curl http://glue-middleware.eu-west-2.elasticbeanstalk.com/externalBotUrl`
- Get list of current chat participants: `curl -w "\n" http://glue-middleware.eu-west-2.elasticbeanstalk.com/chatParticipants`

## Backlog for GUI/Middleware build

1) ~~Tell user what their (randomly generated) name is~~ DONE
2) ~~Allow user to enter their own name~~ decided not to implement to keep things anonymous
3) Improve design. Add logo for GLUE. 
4) Add basic admin panel:
    - Move URL entry to here
    - ~~Observe chat~~ DONE
    - See who is online
    - Reset Alana/GLUE session
5) ~~Add tokenisation within middleware~~ DONE
    - Add `glue respond` to force a response from GLUE.
6) ~~Add logging required to get evaluation metrics (probably easiest to do via log messages that are in a sensible format)~~ DONE - not logs messages are in admin panel as well as log files
7) ~~Add name entry/privacy notice screen~~ decided not needed, consent will be managed offline
8) Add waiting state
9) ~~Add multi-modal input for quiz/games~~ - not needed any more as 'final answer' keyword being used in RASA
10) (Nice to have) Add ASR
11) (Nice to have) Add a more sophisticated timing service:
    - Can we detect a question, and give the user more time?
    - Can we detect when a user is typing, and give them more time?
