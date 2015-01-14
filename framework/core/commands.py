from blessings import Terminal
t = Terminal()
from cmd2 import Cmd as Slither
import sys


class Run(Slither):

    """ Slither command functions
    """

    def __init__(self):
        super().__init__()

    def do_akaspy(self, args):

        """ Usage: akaspy origin target
        """

        try:
            import framework.aux.akaspy as akaspy
        except ImportError as e:
            print(t.red(">>> ") + "Failure To Import Module!\n >>> {0}".format(e))
            sys.exit(1)
        origin, target = args.split()[0], args.split()[1]
        run = akaspy.AkaspyAction(origin, target)
        run.check_origin()

    def do_jnlp(self, args):

        """ Usage: jnlp /path/to/application.jnlp
        """

        try:
            import framework.aux.jnlp_parser as jnlp
        except ImportError as e:
            print(t.red(">>> ") + "Failure To Import Module!\n >>> {0}".format(e))
            sys.exit(1)
        jnlp_file = args.split()[0]
        run = jnlp.jnlp_action(jnlp_file)
        run.jnlp_parse()

    def do_struts2(self, args):

        """ Usage: jnlp /JNLP/File/Path
        """

        try:
            import framework.modules.struts2.struts2_includeParams as struts2_params
        except ImportError as e:
            print(t.red(">>> ") + "Failure To Import Module!\n >>> {0}".format(e))
            sys.exit(1)
        if args.split()[1] == "params":
            run = struts2_params.Struts2IncludeParamsAction(args.split()[0])
            run.check_exec()

    def do_jmap(self, args):

        """ Usage: jmap {Number of Heap Dumps} {ProcessID}
        """

        try:
            from framework.aux.jmap import JmapAction as jmap
        except ImportError as e:
            print(t.red(">>> ") + "Failure To Import Module!\n >>> {0}".format(e))
            sys.exit(1)
        number, pid = args.split()
        run = jmap(int(number), pid)
        run.heap_dump()




