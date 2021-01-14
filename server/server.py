from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Main variables for the server
HOST = 'localhost'
PORT = 5500
BUFFSIZ = 1024
ADDR = (HOST, PORT)

# Initializing the server
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
