import React from 'react';

class ChatInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = { value: '' };

        this.handleChange = this.handleChange.bind(this);
        this.handleSend = this.handleSend.bind(this);
    }

    handleChange(event) {
        this.setState({ value: event.target.value });
    }

    handleSend() {
        this.props.sendMessage(this.state.value);
        this.setState({ value: '' });
    }

    render() {
        return (
            <form>
                <label>
                    Message:
                    <input type="text" value={this.state.value} onChange={this.handleChange} />
                </label>
                <button type="button" value="Send" onClick={this.handleSend}>
                    Send Message
                </button>
            </form>
        );
    }
}

export default ChatInput;