from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Global Constants
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 1024

# Global Variables
messages = []

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)



def recieve_messages():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            messages.append(msg)
            print(msg)        
        except Exception as e:
            print(f"[EXCEPTION] {e}")
            break


def send_message(msg):
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()


recieve_thread = Thread(target=recieve_messages)
recieve_thread.start()

send_message("Maulik")
send_message("Hello World")
