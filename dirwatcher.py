import sys
import signal
import logging
import time

from helper.create_parser import create_parser
from helper.dir_search import dir_search
from helper.find_word import find_word
from helper.log_event import log_event
from helper.watcher import watcher

exit_flag= {"state" : False }

__author__ = 'Scott Reese'


def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here as well (SIGHUP?)
    Basically it just sets a global flag, and main() will exit it's loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """

    signames = dict((k, v) for v, k in reversed(sorted(signal.__dict__.items()))
                    if v.startswith('SIG') and not v.startswith('SIG_'))
    logging.warn('Received ' + signames[sig_num])
    exit_flag["state"] = True


def main(args):
    parser = create_parser()
    start_msg = """
    ------------------------------\n
    Started dirwatcher.py\n
    ------------------------------
    """
    end_msg = """
    ------------------------------\n
    Stopped dirwatcher.py\n
    Uptime was {}\n
    ------------------------------
    """

    if not args:
        parser.print_usage()
        sys.exit(1)
    
    print(start_msg)

    then = time.time()

    parsed_args = parser.parse_args(args)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    __dir, __ext = parsed_args.dir, parsed_args.ext
    polling_interval, magic = float(parsed_args.int), parsed_args.magic
    data = {}

    try:
        for __file in dir_search(__ext, __dir):
            data[__file] = 0
    except TypeError as e:
        log_event(e)

    find_word(data, magic)

    while not exit_flag["state"]:
        try:
            watcher(data, __dir, __ext, magic)
        except Exception as e:
            log_event(e)

        time.sleep(polling_interval)
    run_time = time.time() - then
    print(end_msg.format(str(run_time)))


if __name__ == '__main__':
    main(sys.argv[1:])
