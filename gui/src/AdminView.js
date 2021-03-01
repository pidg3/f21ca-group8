import React from 'react';

import './App.css';

import ChatInput from './chat/ChatInput';
import ChatWindow from './chat/ChatWindow';
import BotUrlInput from './BotUrlInput';

// Swap over the below lines for local development

// const EXPRESS_URL = 'glue-middleware.eu-west-2.elasticbeanstalk.com';
const EXPRESS_URL = 'localhost:8090';

// const SOCKETS_URL = 'glue-middleware.eu-west-2.elasticbeanstalk.com:8080';
const SOCKETS_URL = 'localhost:8080';

const USERNAME = 'Me'; // temporary, till user can enter name

class AdminView extends React.Component {
    constructor(props) {
        super(props);
        this.state = { serverMessages: [] };

        this.appendMessage = this.appendMessage.bind(this);
        this.sendMessage = this.sendMessage.bind(this);
        this.receiveMessage = this.receiveMessage.bind(this);
        this.setUrl = this.setUrl.bind(this);
    }

    componentDidMount() {
        this.setUrl('');
    }

    appendMessage(message) {
        this.setState({ serverMessages: [...this.state.serverMessages, message] });
    }

    receiveMessage(message) {
        console.log(message);
        if (message.data === '~CONNECTED~') {
            this.appendMessage('Helper Bot: connected to GLUE!');
        } else {
            this.appendMessage(message.data);
        }
    }

    render() {
        return (
            <div className="App">
                <h1>Admin View</h1>
                {this.state.serverMessages.map(msg => <p>{msg}</p>)}
            </div>
        );
    }
}

export default AdminView;
