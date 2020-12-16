# TCP ChatRoom

#### This is a chatrrom which I made in python
#### It consists of a server and multiple clients can connect to the server and send messages to each other
#### The messages which are sent are encoded in ascii and then are decoded by the other client for safety

## Modules Used
- threading
- socket

All the modules above are standard modules that come installed with Python 3, so you doon't need to install them

## Steps to use this Chatroom
- Type this command in terminal if you have git installed 
  ```
  git clone https://github.com/IAmMaulik/TCP_ChatRoom.git
  ```
- Run the program by writing ```python server.py```
- Run the client(s) by ```python client.py```


## Points to Improve
- Adding a chatrrom name
- Improving the front-end and adding a GUI
- Adding an admin role, as well as kick and ban features
- Automatic muting feature if someone send a profane message
