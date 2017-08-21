import os
import sys
import time

from data_processor.data_processor import process_data

from support.command_line_parser import parse_command_line
from support.support_funcs import decompress_file, is_file_zipped, print_seconds_nice


def main():
    args = parse_command_line()

    if args.inputfile is None:
        print("ERR: please specify output file")
        exit(1)

    if not os.path.exists(args.inputfile):
        print("ERR: data file does not exists. file name: {}".format(args.inputfile))
        exit(2)

    tm_begin = None
    if args.verbose or args.worktimetostderr:
        tm_begin = time.time()

    if args.limit:
        args.limit = int(args.limit)

    decompressed_file_name = None

    if is_file_zipped(args.inputfile):
        if args.temp_dir is None:
            print("temporary directory is't specified - can't decompress file")
            exit(4)

        decompressed_file_name = decompress_file(args.inputfile, args.temp_dir)
        if decompressed_file_name is None:
            exit(5)

        args.inputfile = decompressed_file_name

    processed_tasks_count = process_input_file(args, decompressed_file_name)

    if args.verbose or args.worktimetostderr:
        seconds_elapsed = round(time.time() - tm_begin, 3)
        msg = "{} - {} tasks processed".format(
            print_seconds_nice(seconds_elapsed, "Done @ "),
            processed_tasks_count
        )

        if args.worktimetostderr:
            sys.stderr.write("{}\n".format(msg))
        else:
            print(msg)


def process_input_file(args, decompressed_file_name):
    output_file = None
    try:
        if args.outputfile is not None:
            output_file = open(args.outputfile, "wt")

        out = output_file if output_file is not None else sys.stdout

        processed_tasks_count = process_data(
            args.inputfile,
            out,
            not args.dontprint,
            args.limit,
            args.verbose
        )
    finally:
        if output_file is not None:
            output_file.close()

        if decompressed_file_name is not None:
            os.remove(decompressed_file_name)

    return processed_tasks_count


if __name__ == "__main__":
    main()
