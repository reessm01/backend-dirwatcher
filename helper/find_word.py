import os
import logging

__author__ = "Scott Reese"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def find_word(files, magic):
    """Checks for and logs if a magic word is found in a list of files

    Arguments:
        files {dict} -- dictionary of files with last position checked
        magic {String} -- magic word to search for

    Returns:
        dict -- modified dictionary containing last line position checked
    """
    for __file in files.keys():
        with open(__file) as f:
            for _ in range(files[__file]):
                f.readline()
            line = f.readline()
            while len(line) > 0:
                if magic.lower() in line.lower():
                    logger.info("{} found at {} on line {}".format(
                        magic, __file, files[__file]))
                line = f.readline()
                files[__file] += 1

    return files
