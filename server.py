import threading
import socket

host = '169.254.15.253'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# We can use this broadcast function to send messages to all the clients in the chatroom
def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nkname = nicknames[index]
            print(f"{nkname} has left the chat!".encode('ascii'))
            nicknames.remove(nkname)
            break

def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {client}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} has joined the chat!".encode('ascii'))
        client.send("Connected to the server".encode('ascii'))


        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


recieve()
