function Servers(serverList){
    this.serverList = serverList;
    this.currentServer = 0;
}

Servers.prototype.next = function(){
    var server = this.serverList[this.currentServer++];
    this.currentServer %= this.serverList.length;
    return server;
};