import os
from optparse import OptionParser
from system.stopwatch import Stopwatch
from system.shared import makeAbsoluteAppPath

import signal
from core.solver import ProblemSolver
import multiprocessing


def signal_handler(signal, frame):
    """
    Handler for Ctrl-C combination. Terminates program execution

    :param signal:
    :param frame:
    :return: None
    """
    print()
    print("Quit by Ctrl-C")
    print()
    exit(0)


def cpu_count():
    return multiprocessing.cpu_count()


def main():
    # parsing command line
    parser = OptionParser()
    parser.add_option("-i", "--inputfile", type=str, dest="input_file", default=None, help="Input file")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose_output", default=False, help="Verbose output")
    parser.add_option("-n", "--notprint", action="store_true", dest="not_print_result", default=False, help="Not print result")
    parser.add_option("-l", "--limit", type=int, dest="limit_output", default=None, help="Limit output")

    (cmd_line_options, args) = parser.parse_args()
    if cmd_line_options.input_file is None:
        print("ERR: please specify input file")
        parser.print_help()
        return -1

    abs_file_name = makeAbsoluteAppPath(cmd_line_options.input_file)
    if not os.path.exists(abs_file_name):
        print("ERR: input file does not exists, file name: {}".format(cmd_line_options.input_file))
        return -2

    watch = Stopwatch(True, True, True)

    solver = ProblemSolver()
    solver.file_name = abs_file_name

    solver.verbose_mode = cmd_line_options.verbose_output
    solver.not_print_result = cmd_line_options.not_print_result
    solver.limit_output = cmd_line_options.limit_output
    solver.threads_count = cpu_count()

    if not solver.process():
        print("ERROR problem solving task: {}".format(solver.errorText))
        return -3

    if cmd_line_options.verbose_output:
        print(watch)
    return 0


if __name__ == "__main__":
    # initializing Ctrl-C handler
    signal.signal(signal.SIGINT, signal_handler)

    res = main()
    exit(res)
