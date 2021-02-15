import React from 'react';

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
            <form onSubmit={this.handleSend}>
                <label>
                    Update External Bot URL:
                    <input type="text" value={this.state.value} onChange={this.handleChange} />
                </label>
                <button type="submit" value="Send">
                    Set URL
                </button>
            </form>
        );
    }
}

export default BotUrlInput;