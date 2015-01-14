import dns.resolver
import socket
import errno

from blessings import Terminal
t = Terminal()

from framework.aux.auxiliary_enums import AuxiliaryEnums
from framework.utils.logger import logger


class AkaspyAction(object):

    def __init__(self, domain, target):

        self.domain = domain
        self.target = target

    def do_bypass(self, ip):

        """ Bypass Akamai
        """

        # Set some shit up first
        port = AuxiliaryEnums.HTTP_PORT
        address = (ip, port.value)
        url = self.target
        request = "GET / HTTP/1.1\r\nHost: {0}\r\n\r\n".format(url)

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(address)
            s.send(request.encode())
            data = s.recv(15)
            if "200" in data.decode('utf-8'):
                logger("info", "Origin Access Possible!")
            else:
                logger("warning", "Origin Access Not Possible! :: {0}".format(t.yellow(data.decode("utf-8"))))

            # Don't forget to close the socket
            s.close()

        except socket.error as e:
            # Handle some exceptions
            if e.errno != errno.ECONNREFUSED:
                logger("warning", "Connection Issue!")
                raise e
            else:
                logger("warning", "Socket Refused!")
                pass

    def check_origin(self):

        """ Check the origin
        """

        try:
            # Set some shit up first
            answer = dns.resolver.query(self.domain)
            if answer.qname == answer.canonical_name:
                logger("warning", "Incorrect DNS Record :: {0}".format(t.yellow(str(answer.qname))))
                logger("info", "Origin Not Accessible!")
            else:
                logger("info", "Retrieved An Alias! :: {0}".format(t.yellow(str(answer.canonical_name))))

            response = dns.resolver.query(answer.canonical_name, 'A')

            for response_data in response:
                ip = response_data.address
                if ip:
                    logger("info", "Getting IP Address :: {0}".format(t.yellow(ip)))
                    self.do_bypass(ip)
        except dns.resolver.NXDOMAIN:
            logger("warning", "Domain Not Found!")
            pass
        except dns.resolver.Timeout:
            logger("warning", "Query Timed Out!")
            pass
        except dns.exception.DNSException:
            logger("warning", "DNS Exception!")
            pass
