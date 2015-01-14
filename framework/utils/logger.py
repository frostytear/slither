from blessings import Terminal
t = Terminal()

import logging


def logger(level_name, msg):

    """ Slither Logger
    """

    levels = {'info': logging.INFO, 'warning': logging.WARNING}
    info = t.green(">>> ") + "%(asctime)-15s %(message)s"
    warning = t.red(">>> ") + "%(asctime)-15s %(message)s"

    if level_name == "info":
        level = levels.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level, format=info)
        return logging.info(msg)

    elif level_name == "warning":
        level = levels.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level, format=warning)
        return logging.warning(msg)

    else:
        print(t.red(">>> ") + "Incorrect Log Level!")