import React from 'react';

import './App.css';

// Swap over the below lines for local development

const EXPRESS_URL = 'glue-middleware.eu-west-2.elasticbeanstalk.com';
// const EXPRESS_URL = 'localhost:8090';

const SOCKETS_URL = 'glue-middleware.eu-west-2.elasticbeanstalk.com:8080';
// const SOCKETS_URL = 'localhost:8080';

class AdminView extends React.Component {
    constructor(props) {
        super(props);
        this.state = { serverMessages: [] };

        this.appendMessage = this.appendMessage.bind(this);
        this.receiveMessage = this.receiveMessage.bind(this);
        this.connect = this.connect.bind(this);
    }

    componentDidMount() {
        this.connect();
    }

    appendMessage(message) {
        this.setState({ serverMessages: [...this.state.serverMessages, message] });
    }

    receiveMessage(message) {
        if (message.data === '~CONNECTED~') {
            this.appendMessage('Helper Bot: connected to GLUE!');
        } else {
            this.appendMessage(message.data);
        }
    }

    async connect() {
        this.connection = new WebSocket(`ws://${SOCKETS_URL}?type=admin`);

        this.connection.onmessage = (msg) => {
            this.receiveMessage(msg);
        }
    }

    render() {
        return (
            <div className="App">
                <h1>Admin View</h1>
                {this.state.serverMessages.map(msg => <span>{msg}<br/></span>)}
            </div>
        );
    }
}

export default AdminView;
