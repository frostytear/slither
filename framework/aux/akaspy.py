import dns.resolver
import socket
import errno
from blessings import Terminal
from framework.aux.auxiliary_enums import AuxiliaryEnums
t = Terminal()


class akaspy_command(object):

    def __init__(self, domain, target):
        self.domain = domain
        self.target = target

    def do_bypass(self, ip):

        # Setup socket parameters
        port = AuxiliaryEnums.HTTP_PORT
        address = (ip, port.value)
        url = self.target
        request = "GET / HTTP/1.1\r\nHost: {0}\r\n\r\n".format(url)

        try:
            # Create socket connection and HTTP request
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(address)
            s.send(request.encode())
            data = s.recv(15)
            code = "200"

            # Check HTTP response code
            if code in data.decode('utf-8'):
                print(t.green(">>> ") + "Origin Access Possible!")
            else:
                print(t.red(">>> ") + "Origin Access Not Possible")
                print(t.red(">>> ") + "HTTP Status Code :: {0}".format(data.decode('utf-8')))

            s.close()

        except socket.error as e:

            if e.errno != errno.ECONNREFUSED:
                print(t.red(">>> ") + "Connection Issue!")
                raise e
            else:
                print(t.red(">>> ") + "Socket Refused!")
                pass

    def check_origin(self):

        try:

            answer = dns.resolver.query(self.domain)

            # Check for DNS record
            if answer.qname == answer.canonical_name:
                print(t.red(">>> ") + "Incorrect DNS Record :: {0}".format(answer.qname))
                print(t.red(">>> ") + "Origin Not Accessible")
            else:
                print(t.green(">>> ") + "Retrieved an alias! :: {0}".format(answer.canonical_name))

            response = dns.resolver.query(answer.canonical_name, 'A')

            for response_data in response:
                ip = response_data.address
                if ip:
                    print(t.green(">>> ") + "Getting IP Address :: {0}".format(ip))

                    # Try the origin bypass
                    self.do_bypass(ip)

        except dns.resolver.NXDOMAIN:
            print(t.red(">>> ") + "Domain Not Found!")
            pass
        except dns.resolver.Timeout:
            print(t.red(">>> ") + "Query Timed Out!")
            pass
        except dns.exception.DNSException:
            print(t.red(">>> ") + "DNS Exception!")
            pass
