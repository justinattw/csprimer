# Communicate with this server by `nc -u 127.0.0.1 9999`

import socket

# open a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bound to a port
s.bind(("0.0.0.0", 9999))

while True:

    # Receive from a port
    msg, sender = s.recvfrom(4096)

    print(f'Received {msg.decode("utf8")} from {sender}')
    
    # make data shouty

    # Send (back) to the port
    s.sendto(msg, sender)
    

