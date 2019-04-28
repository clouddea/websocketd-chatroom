from WebsocketServer import WebsocketServer, WebSocketHandler
from subprocess import call,Popen, PIPE, CREATE_NEW_CONSOLE
from threading import Thread
import sys
import io
fileArray = {}

def new_client_thread(client, server):
    while True:
        line1 = (fileArray[client.get("id")].stdout.readline())
        line2 = (fileArray[client.get("id")].stdout.readline())
        if not (line1 and line2):
            break
        try:
            if int(line1) == 0 and client in server.clients:
                server.send_message(client, line2)
            elif int(line1) == 1:
                #print(line2)
                server.send_message_to_all(line2)
            elif int(line1) == 2:
                line3 = (fileArray[client.get("id")].stdout.readline())  # destination
                clients_id = line3.strip().split(",")
                for cli_id in clients_id:
                    for cli in server.clients:
                        if str(cli.get("id")) == cli_id:
                            server.send_message(cli, line2)
        except ValueError as e:
            print("Error: Msg format error.")
            print(e)

    print("thread over")

def new_client(client, server):
    print(str(client.get("address")) + " entry")
    fileArray[client.get("id")] = Popen(sys.argv[2:], stdin=PIPE, stdout=PIPE, shell=True, encoding="utf-8", bufsize=0)
    print(client.get("id"), file = fileArray[client.get("id")].stdin)
    Thread(target = new_client_thread, args=(client, server)).start()         #start thread to read stdout

def message_received(client, server, message):
    print(message, file = fileArray[client.get("id")].stdin)

def client_left(client, server):
    print("user " + str(client.get("id")) + " left")
    fileArray[client.get("id")].stdin.close()                     #close the stream



server = WebsocketServer(int(sys.argv[1]), "0.0.0.0")
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.set_fn_client_left(client_left)
print("serverStart on port %s......"%(sys.argv[1],))
server.serve_forever()

