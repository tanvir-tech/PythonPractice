import socket
import sys

try:
    s = socket.socket()                                                         # creating socket object
    print("Client socket created")
except socket.error as err:
    print("Client socket creation failed",str(err))
    sys.exit()

server_ip = input("Enter the server name :")
server_port = int(input("Enter the port :"))
data_in_Bytes = bytes(input("Enter your name :"), 'utf-8')                       # byte encoding

try:
    s.connect((server_ip, server_port))                                          # Conneting socket with server
    print(f"Connected to {server_ip} server at port {server_port}!")
    s.send(data_in_Bytes)                                                        # sending bytes

    print("Server says :",s.recv(1024).decode())                                 # Receiving bytes and  Decoding
    s.shutdown(2)                                                                # shutdown socket after finishing tasks
except socket.error as er:
    print("Connection failed ! Reason is :",str(er))
    sys.exit()

