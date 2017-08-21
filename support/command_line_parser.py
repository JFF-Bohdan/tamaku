import argparse


def parse_command_line():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--inputfile",
        metavar="FILE",
        help="input file with tasks"
    )

    parser.add_argument(
        "-o",
        "--outputfile",
        metavar="FILE",
        help="output file for results"
    )

    parser.add_argument(
        "-t",
        "--temp_dir",
        metavar="store",
        help="temporary folder (for decompressing files)"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output",
        default=False
    )

    parser.add_argument(
        "-w",
        "--worktimetostderr",
        action="store_true",
        help="Write work time to stderr",
        default=False
    )

    parser.add_argument(
        "-n",
        "--dontprint",
        action="store_true",
        help="Do not print result"
    )

    parser.add_argument(
        "-l",
        "--limit",
        action="store",
        help="Limit output"
    )

    return parser.parse_args()
