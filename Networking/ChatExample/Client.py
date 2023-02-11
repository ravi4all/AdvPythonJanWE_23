import socket

s = socket.socket()
port = 9999

s.connect(('localhost',port))
# 1024 bytes = 1KB
msg = input("Enter your message : ")

while True:
    s.send(msg.encode())
    data = s.recv(1024).decode()
    print("Server :",data)
    msg = input("Enter your message : ")

s.close()