import sys
import io
import json
import psycopg2
from urllib import request
from urllib.parse import quote
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = "utf-8")

def dump(obj):
    return json.dumps(obj, ensure_ascii = False)

obj = {}
id = input()
nickName = input()
request.urlopen("http://localhost:8082/add?id=%s&nickName=%s"%(id,quote(nickName)))




obj["nickName"] = "系统管理员"
obj["type"] = 1
obj["content"] = """{"type":0,"content" : "欢迎来到聊天室。你的id是:%s,请不要刷屏和发送违法的内容。"}"""%(id,)
print(0)
print(dump(obj))

obj["nickName"] = nickName
obj["type"] = 0
print(1)
print(dump(obj))



#process start
while True:
    obj["type"] = 1
    try:
        inputContent = input()
        if inputContent == "heartbeating":
            f = request.urlopen("http://localhost:8082/selectNickName")
            obj["type"] = 3
            obj["content"] = json.loads(f.read().decode("utf-8"))
            print(0)
            print(dump(obj))
            continue
        obj["content"] = inputContent
        print(1)
        print(dump(obj))
    except EOFError:
        break
#process over


obj["type"] = 2
obj["content"] = """{"type" : 0, "content" : ""}"""
print(1)
print(dump(obj))
request.urlopen("http://localhost:8082/remove?id=%s"%(id,))
