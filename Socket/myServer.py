import socket

s = socket.socket()                     # create a socket
# print("socket created")

s.bind(("localhost",9999))              # bind takes a tuple server-IP and Port
s.listen(1)                             # server lisens for  5 client-connections
print("waiting for connection...")


while True:
    connection1, addr = s.accept()                          # accept & returns a CONNECTION with address

    name = connection1.recv(1024).decode()                  # receiving at bufsize 1024
    print("connected with : ",addr,name)

    connection1.send(bytes("welcome myClient",'utf-8'))     # sending bytes at text formate

    connection1.close()                                     # closing CONNECTION








