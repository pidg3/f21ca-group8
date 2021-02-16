# F21CA - Group 8

This is a monorepo containing the three parts of our code:

- `/gui`: front end, basic chat window. Hosted here: http://glue-bot.s3-website.eu-west-2.amazonaws.com/. Deploys automatically to S3 with a push to `master`. 
- `/middleware`: node service providing basic message forwarding for multi-party chat, issuing of requests to Alana/GLUE, and loggig of statistics for evaluation. Hosted here: http://glue-middleware.eu-west-2.elasticbeanstalk.com. Requires manual deployment to Elastic Beanstalk.
- `/rasa`: Python code implementing our GLUE bot (note, this will be accessed as an Alana bot). Requires hosting via nGrok or similar tool, and the URL passing into the GUI. 