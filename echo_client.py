import socket
import sys

host = 'localhost'
port = 50000
size = 1024
s = None


def echo_client(message):
    if len(sys.argv) > 1:
        message = sys.argv[1]
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
    except socket.error, (value, message):
        if s:
            s.close()
        print "Could not open socket: " + message
        sys.exit(1)
    s.send(message)
    data = s.recv(size)
    s.close()
    return 'Received:', data

if __name__ == '__main__':
    message = echo_client('Hello')
    print "{} {}".format(message[0], message[1])
