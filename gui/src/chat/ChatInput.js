import React from 'react';
import { Button, TextField } from '@material-ui/core';

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

    handleSend(e) {
        e.preventDefault();
        this.props.sendMessage(this.state.value);
        this.setState({ value: '' });
    }

    render() {
        return (
            <form className="text-submit" onSubmit={this.handleSend}>
                <TextField
                    value={this.state.value}
                    autoFocus={true}
                    id="outlined-multiline-static"
                    label="Message"
                    variant="outlined"
                    onChange={this.handleChange}
                />
                <Button
                    style={{marginLeft: 10}}
                    color="primary"
                    variant="contained"
                    type="submit"
                    value="Send"
                >
                    Send Message
                </Button>
            </form>
        );
    }
}

export default ChatInput;