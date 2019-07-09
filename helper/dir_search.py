import os

from helper.log_event import log_event

__author__ = "Scott Reese"

def dir_search(ext, file_path = './'):
    """Searches for files based on path and extension. Returns list of files found.
    
    Arguments:
        ext {string} -- extension of files to be searched
    
    Keyword Arguments:
        file_path {str} -- file path to find files (default: {'./'})

    Returns:
        {list} -- list of filenames
    """
    try:
        return [file_path + "/" + file for file in os.listdir(file_path) if file.endswith(ext)]
    except OSError as e:
        log_event(e)