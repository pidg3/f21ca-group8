import React from 'react';

import './App.css';

import ChatInput from './chat/ChatInput';
import ChatWindow from './chat/ChatWindow';
import BotUrlInput from './BotUrlInput';

// Swap over the below lines for local developmenet

const SERVER_URL = 'glue-middleware.eu-west-2.elasticbeanstalk.com';
// const SERVER_URL = 'localhost';

const USERNAME = 'Me'; // temporary, till user can enter name

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { serverMessages: [] };

    this.appendMessage = this.appendMessage.bind(this);
    this.sendMessage = this.sendMessage.bind(this);
    this.receiveMessage = this.receiveMessage.bind(this);
    this.setUrl = this.setUrl.bind(this);
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
    if (message.data === '~CONNECTED~') {
      this.appendMessage('Helper Bot: connected to Alana!');
    } else {
      this.appendMessage(message.data);
    }
  }

  async setUrl(url) {
    const response = await fetch(`http://${SERVER_URL}/setExternalBotUrl`, {
      method: 'POST',
      mode: 'cors',
      cache: 'no-cache',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ externalBotUrl: url})
    });
    console.log(response);
    this.connection = new WebSocket(`ws://${SERVER_URL}:8080`);

    this.connection.onmessage = (msg) => {
      this.receiveMessage(msg);
    }

  }

  render() {
    return (
      <div className="App">
        <ChatWindow messages={this.state.serverMessages} />
        <ChatInput sendMessage={(message) => this.sendMessage(message)} />
        <BotUrlInput setUrl={(url) => this.setUrl(url)}/>
      </div>
    );
  }
}

export default App;
