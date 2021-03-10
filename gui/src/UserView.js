import React from 'react';
import { Button } from '@material-ui/core';

import './App.css';

import ChatInput from './chat/ChatInput';
import ChatWindow from './chat/ChatWindow';

// Swap over the below lines for local development

const EXPRESS_URL = 'glue-middleware.eu-west-2.elasticbeanstalk.com';
// const EXPRESS_URL = 'localhost:8090';

const SOCKETS_URL = 'glue-middleware.eu-west-2.elasticbeanstalk.com:8080';
// const SOCKETS_URL = 'localhost:8080';

const USERNAME = 'Me'; // temporary, till user can enter name

class UserView extends React.Component {
  constructor(props) {
    super(props);
    this.state = { serverMessages: [], connected: false };

    this.appendMessage = this.appendMessage.bind(this);
    this.sendMessage = this.sendMessage.bind(this);
    this.receiveMessage = this.receiveMessage.bind(this);
    this.connect = this.connect.bind(this);
  }

  appendMessage(message) {
    this.setState({ serverMessages: [message, ...this.state.serverMessages] });
  }

  sendMessage(message) {
    if (this.connection !== undefined) {
      this.connection.send(message);
      this.appendMessage(`${USERNAME}: ${message}`);
    } else {
      this.appendMessage('Helper Bot: sorry, not connected');
    }
  }

  receiveMessage(message) {
    console.log(message);
    if (message.data.includes('~CONNECTED#') === true) {
      const username = message.data.split('#')[1];
      this.appendMessage(`Helper Bot: connected to GLUE as ${username}!`);
    } else {
      this.appendMessage(message.data);
    }
  }

  async connect() {
    this.connection = new WebSocket(`ws://${SOCKETS_URL}`);

    this.connection.onmessage = (msg) => {
      this.setState({connected: true})
      this.receiveMessage(msg);
    }
  }

  render() {
    return (
      <div className="App">
        <ChatWindow messages={this.state.serverMessages} />
        <ChatInput sendMessage={(message) => this.sendMessage(message)} />
        {this.state.connected === false ? 
          <Button
            style={{ marginLeft: 10, width: '20%' }}
            color="default"
            variant="contained"
            type="submit"
            value="Connect"
            onClick={this.connect}
          >
            Connect
        </Button>
        :
        null
      }
      </div>
    );
  }
}

export default UserView;
