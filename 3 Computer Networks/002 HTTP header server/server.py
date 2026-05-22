"""
Use with `curl 127.0.0.1:9999`

Or go to `localhost:9999`
"""

import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 9999))
s.listen()
print(f"Listening for new connections on port 9999")

while True:
    conn, addr = s.accept()
    print(f"New connection from {addr}")

    req = conn.recv(4096)
    headers, body = req.split(b'\r\n\r\n')
    d = {}

    for hline in headers.split(b'\r\n')[1:]:
        k, v = hline.split(b': ')
        d[k.decode('ascii')] = v.decode('ascii')

    conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
    conn.send(json.dumps(d, indent=4).encode('ascii'))

    conn.close()
    