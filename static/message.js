function message(type, content)
{
    /*
        type: 0 plain text, 1 picture
    */
    this.type = type;
    this.content = content;
}

message.prototype.tostring = function(){
    return JSON.stringify(this);
}

function getMessage(type, content){
    JSON.stringify({type : type, content : content});
}