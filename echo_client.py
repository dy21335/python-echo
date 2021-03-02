import socket
import sys
import time

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


try:
    s.connect((HOST, PORT))
except socket.error , msg:
    print 'Connect failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

id = 0

while 1:
    time.sleep(1)
    id += 1
    message = "testing message" + str(id)
    s.sendall(message)
    if id > 10:
        s.sendall('')
        break
    data = s.recv(1024)
    print data