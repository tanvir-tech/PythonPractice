import socket

s = socket.socket()

s.connect(("localhost",9999))


name = input("Enter your name : ")
s.send(bytes(name,'utf-8'))


# receiving
print(s.recv(1024).decode())





