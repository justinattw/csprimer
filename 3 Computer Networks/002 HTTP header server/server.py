"""
goal: accept a connection, echo back anything received
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 9999))
s.listen()
print(f"Listening for new connections on port 9999")

while True:
    conn, addr = s.accept()
    print(f"New connection from {addr}")

    while True:
        data = conn.recv(4096)
        print(f"Received: {data}")
        if not data:
            break
        conn.sendto(data)

    conn.close()
    