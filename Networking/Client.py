import socket

s = socket.socket()
port = 9999

s.connect(('localhost',port))
# 1024 bytes = 1KB
data = s.recv(1024)
print(data)
s.close()