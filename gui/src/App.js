import React from 'react';

import './App.css';

import ChatInput from './chat/ChatInput';
import ChatWindow from './chat/ChatWindow';

const url = 'ws://localhost:8080';
const connection = new WebSocket(url);

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { serverMessages: [] };

    connection.onmessage = (msg) => {
      this.receiveMessage(msg);
    }

    this.sendMessage = this.sendMessage.bind(this);
    this.receiveMessage = this.receiveMessage.bind(this);
  }

  sendMessage(message) {
    connection.send(message);
  }

  receiveMessage(message) {
    this.setState({ serverMessages: [...this.state.serverMessages, message.data]});
  }

  render() {
    return (
      <div className="App">
        <ChatWindow messages={this.state.serverMessages} />
        <ChatInput sendMessage={(message) => this.sendMessage(message)} />
      </div>
    );

  }
}

export default App;
