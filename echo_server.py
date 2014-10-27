import socket
import sys

host = ''
port = 50000
backlog = 5
size = 1024
s = None


def echo_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(backlog)
    except socket.error, (value, message):
        if s:
            s.close()
        print "Could not open socket: " + message
        sys.exit(1)
    while True:
        client, address = s.accept()
        data = client.recv(size)
        if data:
            client.send(data)
        client.close()

if __name__ == '__main__':
    echo_server()
