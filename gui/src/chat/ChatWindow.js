export default (props) => {
    return props.messages.map((msg, idx) => <p key={idx}>{msg}</p>);
};
