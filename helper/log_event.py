import logging


def log_event(msg, type="default"):
    """Logs to the console a message with a time stamp

    Arguments:
        msg {String} -- message to be communicated
    """
    if type == "default":
        FORMAT = '%(asctime)-15s %(message)s'
    else:
        FORMAT = ""
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger('dirwatcher')
    logger.setLevel(logging.INFO)
    logger.info(msg)
