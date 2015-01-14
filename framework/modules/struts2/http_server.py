import socketserver
from http.server import BaseHTTPRequestHandler

# Setup terminal colors
from blessings import Terminal
t = Terminal()

""" Struts HTTP Server """


class HTTPHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        print(t.yellow(">>> Download Detected! :: {0} {1} {2} {3}".format(self.command, self.path,
                                                                          self.protocol_version,
                                                                          200)))
        self.end_headers()

    # Override log_message()
    def log_message(self, format, *args):
        return


class HTTPServer(object):

    def __init__(self, address, port):

            self.address = address
            self.port = int(port)

    def run(self):

            httpd = socketserver.TCPServer((self.address, self.port), HTTPHandler)
            print(t.green(">>> ") + "HTTP Server Started")

            try:
                httpd.handle_request()

            except Exception as e:
                print(t.red(">>> ") + "Problem Starting HTTP Server!")
                raise e

if __name__ == '__main__':

    try:
        server = HTTPServer("0.0.0.0", 8000)
        server.run()
    except KeyboardInterrupt:
        print(t.green(">>> ") + "Exiting HTTP Server!")