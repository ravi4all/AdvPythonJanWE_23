import socket

s = socket.socket()

port = 9999
s.bind(('localhost', port))
print("Socket binded to",port)

s.listen(5)
print("Socket is listening...")
print("Waiting for client to connect...")
msg = "Thankyou for connecting with us..."

while True:
    # accept connection from client
    conn, address = s.accept()
    print("Got connection from",address)
    # encode - convert string to bytes
    conn.send(msg.encode())
    conn.close()