#!/usr/bin/env python

from framework.core.commands import Run
from blessings import Terminal
t = Terminal()


def main():

    print(t.green("""

  _________.__   .__   __   .__
 /   _____/|  |  |__|_/  |_ |  |__    ____  _______
 \_____  \ |  |  |  |\   __\|  |  \ _/ __ \ \_  __ |
 /        \|  |__|  | |  |  |   Y  \   ___/  |  | \/
/_______  /|____/|__| |__|  |___|  / \___  > |__|
        \/                       \/      \/


    """))

    slither = Run()
    slither.prompt = t.green("(slither) ")
    slither.ruler = t.green("-")
    slither.cmdloop()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as interrupt:
        print(t.green(">>>") + "Keyboard Interrupt")



