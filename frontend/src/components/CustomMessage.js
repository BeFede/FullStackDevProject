const CustomMessage = (props) => {
    let color = "";
    switch(props.type){
        case 'normal':
            color = "black"
            break;
        case 'success':
            color = "green"
            break;
        case 'error':
            color = "red"
            break;
        default:
            color = 'black'
    }
    
    return (
        <div style={{height:50, marginTop: 25}}>
            <span style={{color: color}}>{props.children}</span>
        </div>
    );
}

export default CustomMessage;