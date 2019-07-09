import sys
import signal
import logging
import time

from helper.signal_handler import signal_handler
from helper.create_parser import create_parser
from helper.dir_search import dir_search
from helper.find_word import find_word
from helper.log_event import log_event
from helper.watcher import watcher

exit_flag = False

__author__ = 'Scott Reese'

def main(args):
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    __dir, __ext = parsed_args.dir, parsed_args.ext
    polling_interval, magic = parsed_args.int, parsed_args.magic
    data = {}

    try:
        for __file in dir_search(__ext, __dir):
            data[__file] = 0
    except TypeError as e:
        log_event(e)

    find_word(data, magic)

    while not exit_flag:
        try:
            watcher(data,__dir,__ext,magic)
        except Exception as e:
            log_event(e)

        time.sleep(polling_interval)

    # final exit point happens here
    # Log a message that we are shutting down
    # Include the overall uptime since program start.


if __name__ == '__main__':
    main(sys.argv[1:])
