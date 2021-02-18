import React from 'react';
import { Button, TextField, Paper } from '@material-ui/core';

class BotUrlInput extends React.Component {
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
        this.props.setUrl(this.state.value);
        this.setState({ value: '' });
    }

    render() {
        return (
            <form 
                className="text-submit"
                onSubmit={this.handleSend}
            >
                <TextField
                    value={this.state.value}
                    autoFocus={true}
                    id="outlined-multiline-static"
                    label="Set External Bot URL"
                    variant="outlined"
                    onChange={this.handleChange}
                />
                <Button
                    style={{ marginLeft: 10 }}
                    color="default"
                    variant="contained"
                    type="submit"
                    value="Send"
                >
                    Connect
            </Button>
            </form>
        );
    }
}

export default BotUrlInput;