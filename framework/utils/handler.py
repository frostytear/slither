from blessings import Terminal
t = Terminal()

import socketserver
import socket
import select
import sys


class TCP(socketserver.TCPServer):

    """ http://stackoverflow.com/questions/10085996/shutdown-socketserver-serve-forver-in-one-thread-python-application """

    address_family = socket.AF_INET
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass)
        self.__shutdown_request = False

    def serve_forever(self, poll_interval=0.5):

        # Override that can be shutdown from a request handler
        # This gets called if the handler receivers the 'quit' command

        try:
            while not self.__shutdown_request:
                r, w, e = socketserver._eintr_retry(select.select, [self], [], [], poll_interval)

                if self in r:
                    self._handle_request_noblock()

        finally:
            self.__shutdown_request = False


class Handler(socketserver.BaseRequestHandler):

    def handle(self):

        try:
            if self.request.recv(1024).strip().decode("utf-8") == "ready":
                while True:
                    command = input(t.green(">>> "))
                    self.request.sendall(bytes(command, "utf-8"))
                    print(self.request.recv(2048).decode())
                    if command == 'quit':
                        self.server._shutdown_request = True
        except Exception as e:
            print(t.red(">>> ") + "Error!")
            raise e


if __name__ == "__main__":

    ip, port = socket.gethostbyname(socket.gethostname()), 8001

    try:
        server = socketserver.TCPServer((ip, port), Handler)
        server.serve_forever()
    except OSError as e:
        print(t.red(">>> ") + "Cannot Start Handler!")
        raise e




