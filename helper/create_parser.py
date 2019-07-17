import argparse


def create_parser():
    """Returns an arg parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Directory to watch.')
    parser.add_argument('-e', '--ext', help='File extension to watch.', default=".txt")
    parser.add_argument('magic', help='Text to watch for.')
    parser.add_argument('-i', "--int", help='Polling interval.', default=1.0)

    return parser
