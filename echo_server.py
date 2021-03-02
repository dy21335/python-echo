import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)

PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Server Socket created'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

# this expamle can only response to one client
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
while True:
    data = conn.recv(1024)
    print 'Accept data From Client...' + data
    reply = 'Reply From Server...' + data
    if not data: 
        print 'not data'
        break
    conn.sendall(reply)

conn.close()
s.close()

