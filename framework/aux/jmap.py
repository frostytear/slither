from blessings import Terminal
t = Terminal()
import subprocess


class JmapAction(object):

    def __init__(self, num, pid):

        self.num = num
        self.pid = pid

    def heap_dump(self):

        try:
            for n in range(self.num):
                p = subprocess.Popen("jmap -dump:format=b,file=heap{0}.bin {1}".format(str(n), self.pid), shell=True)
                p.wait()
        except subprocess.CalledProcessError:
            print(t.red(">>> ") + "Process Error!")
        except ValueError:
            print(t.red(">>> ") + "Argument Error!")
