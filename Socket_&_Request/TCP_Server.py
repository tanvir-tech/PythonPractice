import socket
import sys

s = socket.socket()                                         # creating socket object

host_ip = "localhost"
host_port = 9999
s.bind((host_ip,host_port))                                 # bind takes 1 tuple of Server-IP and Port

s.listen(5)                             # listen takes backlog -- if server busy then 5 client will wait and other will be rejected
print("waiting for connection...")

while True:
    connection1, addr = s.accept()                          # accept & returns a CONNECTION and Address

    name = connection1.recv(1024).decode()                  # receiving bytes and Decoding
    print("connected with : ",addr,name)

    connection1.send(bytes(f"Welcome {name} !",'utf-8'))    # sending bytes after Encoding

    connection1.close()                                     # closing connection

