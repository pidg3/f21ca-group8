import { Paper } from '@material-ui/core';

export default (props) => {
    console.log('chat window props', props)
    return (
        <Paper className="chat-window" style={{
            padding: '10px 20px 10px 20px',
            marginTop: 20,
            width: '600px',
            maxHeight: '600px',
            overflow: 'auto',
            display: 'flex',
            flexDirection: 'column-reverse' // gets scroll bar to stick to bottom
        }}>
            {getContent(props.messages)}
        </Paper>
    )
};

const getContent = (messages) => {
    if (messages !== undefined && messages.length > 0) {
        return messages.map((msg, idx) => <p key={idx}>{msg}</p>)
    } else {
        return <p className="no-message-info">No messages yet! Press 'Connect'</p>
    }
}