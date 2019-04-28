from flask import *
from time import *
import json
app = Flask("__main__")

clients = {}

@app.route("/add")
def add():
    clients[request.args.get("id")] = {"enterTime" : localtime(), "nickName" : request.args.get("nickName")}
    return "OK";

@app.route("/remove")
def remove():
    clients.pop(request.args.get("id"));
    return "OK";
    
@app.route("/selectNickName")
def select():
    re = [];
    for value in clients.values():
        re.append(value["nickName"]);
    return json.dumps(re, ensure_ascii = False).encode("utf-8");
    











app.run(host = "0.0.0.0", port = 8082)
