import socket

s = socket.socket()

port = 9999
s.bind(('localhost', port))
print("Socket binded to",port)

s.listen(5)
print("Socket is listening...")
print("Waiting for client to connect...")
# msg = "Thankyou for connecting with us..."
# accept connection from client
conn, address = s.accept()
print("Got connection from",address)
while True:
    # decode - convert bytes to string
    data = conn.recv(1024).decode()
    print("Client :",data)
    msg = input("Enter your message : ")
    # encode - convert string to bytes
    conn.send(msg.encode())

conn.close()