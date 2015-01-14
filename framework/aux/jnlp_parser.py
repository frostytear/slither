import sys
import os
from xml.dom import minidom
import requests
from blessings import Terminal
t = Terminal()


class jnlp_action(object):

    def __init__(self, jnlp):
        self.jnlp = jnlp

    def jnlp_parse(self):

        # Get instance of the XML document, and find appropriate tags
        try:
            doc = minidom.parse(self.jnlp)
            jars = doc.getElementsByTagName("jar")
            codebase = doc.getElementsByTagName("jnlp")
        except TypeError:
            print(t.red(">>> ") + "Bad JNLP File!")
            sys.exit(1)

        # Parse tags and download JAR(s)
        if jars and codebase:
            try:
                for tag in codebase:
                    url = tag.getAttribute("codebase")
                    if url:
                        for jar in jars:
                            jar_file = jar.getAttribute("href").split('/')[-1]
                            r = requests.get("{0}/{1}".format(url, jar.getAttribute("href")), stream=True)
                            with open(os.path.join(os.getcwd() + "/framework/jars/{0}".format(jar_file)), "wb") as f:
                                print(t.green(">>> ") + "Downloading {0}".format(jar_file))
                                for chunk in r.iter_content(chunk_size=1024):
                                    if chunk:
                                        f.write(chunk)
                                        f.flush()
            except TypeError:
                print(t.red(">>> ") + "Unable To Parse JNLP!")
                pass
