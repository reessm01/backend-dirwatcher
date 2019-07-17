from helper.dir_search import dir_search
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def init_data(__ext, __dir):
    """Initializes the files data dict with info from the directory and targeted extension

    Arguments:
        __ext {String} -- targeted file extension
        __dir {String} -- targeted directory location

    Returns:
        [dict] -- dictionary of files with the targeted extension with initialization of starting line
    """
    data = {}
    try:
        for __file in dir_search(__ext, __dir):
            data[__file] = 0
    except Exception as e:
        logger.error(e)

    return data
