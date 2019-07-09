import logging
import signal

__author__ = "Scott Reese"

def signal_handler(sig_num, frame):
    """
    This is a handler for SIGTERM and SIGINT. Other signals can be mapped here as well (SIGHUP?)
    Basically it just sets a global flag, and main() will exit it's loop if the signal is trapped.
    :param sig_num: The integer signal number that was trapped from the OS.
    :param frame: Not used
    :return None
    """
    # log the associated signal name (the python3 way)
    logger = logging.getLogger('tcpserver')
    logger.warn('Received ' + signal.Signals(sig_num).name)
    # log the signal name (the python2 way)
    signames = dict((k, v) for v, k in reversed(sorted(signal.__dict__.items()))
                    if v.startswith('SIG') and not v.startswith('SIG_'))
    logger.warn('Received ' + signames[sig_num])
    exit_flag = True