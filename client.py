import socket
import threading

nickname = str(input("Enter your nickname: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('169.254.15.253', 55555)) 

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message=='NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An unknown error occurred")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()