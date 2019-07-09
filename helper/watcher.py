from helper.dir_search import dir_search
from helper.find_word import find_word
from helper.log_event import log_event

__author__ = "Scott Reese"

def watcher(data, file_path, __ext, magic):
    """Filters out if there were new files added to the file path, 
    adds and searches for the magic word. Removes as needed if
    file was deleted.

    Arguments:
        data {dict} -- dictionary of existing files
        file_path {String} -- file path to search for files in
        __ext {String} -- desired extension of file to be found
        magic {String} -- magic word to search for
    """
    init_list = data.keys()
    new_entries = list(set(init_list) - set(dir_search(__ext, file_path)))
    new_entry = "new file found {}"
    remove_entry = "file removed {}"

    for entry in new_entries:
        if entry not in init_list:
            data[entry] = 0
            log_event(new_entry.format(entry))
        else:
            del data[entry]
            log_event(remove_entry.format(entry))

    find_word(data, magic)
