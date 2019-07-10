import logging


def log_event(msg):
    """Logs to the console a message with a time stamp

    Arguments:
        msg {String} -- message to be communicated
    """

    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger('dirwatcher')
    logger.setLevel(logging.INFO)
    logger.info(msg)
