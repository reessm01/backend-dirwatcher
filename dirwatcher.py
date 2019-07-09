import sys
import signal
import logging
import time

from helper.signal_handler import signal_handler
from helper.create_parser import create_parser
from helper.dir_search import dir_search

exit_flag = False

__author__ = 'Scott Reese'


def main(args):
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    # Hook these two signals from the OS ..
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    __dir, __ext = parsed_args.dir, parsed_args.ext
    polling_interval, magic = parsed_args.int, parsed_args.magic
    
    init_files = dir_search(__ext, __dir)
    # Now my signal_handler will get called if OS sends either of these to my process.

    # while not exit_flag:
    #     try:
    #         pass
    #        # call my directory watching function.
    #     except Exception as e:
    #         pass
    #         # This is an UNHANDLED exception
    #         # Log an ERROR level message here

    #         # put a sleep inside my while loop so I don't peg the cpu usage at 100%
    #     time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start.


if __name__ == '__main__':
    main(sys.argv[1:])
