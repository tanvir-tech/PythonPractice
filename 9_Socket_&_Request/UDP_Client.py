import socket

UDP_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SMS_in_Bytes = bytes("I am a UDP Client", 'utf-8')

client_ip = "127.0.0.1"
client_port = 9999

UDP_Socket.sendto( SMS_in_Bytes, (client_ip, client_port))

data,address=UDP_Socket.recvfrom(4096)
print("Server says :",str(data))

UDP_Socket.close()