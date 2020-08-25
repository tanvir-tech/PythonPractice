import socket

UDP_Socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP_Socket.bind(("localhost",9999))

while True:
    payload,address = UDP_Socket.recvfrom(4096)
    print(f"{address} client says : {str(payload)}")


    payload = "I am a UDPserver"
    UDP_Socket.sendto(bytes(payload,"utf-8"),address)
