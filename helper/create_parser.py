import argparse

def create_parser():
    """Returns an arg parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Directory to watch.')
    parser.add_argument('ext', help='File extension to watch.')
    parser.add_argument('magic', help='Text to watch for.')
    parser.add_argument('--int', "-i", help='Polling interval.', default=1.0)

    return parser