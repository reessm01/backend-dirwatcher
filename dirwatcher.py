import argparse
import sys

__author__ = 'Scott Reese'

def create_parser():
    """Returns an arg parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Directory to watch.')
    parser.add_argument('ext', help='File extension to watch.')
    parser.add_argument('magic', help='Text to watch for.')
    parser.add_argument('--int', "-i", help='Polling interval.', default=1.0)

    return parser

def main(args):
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)

    parsed_args = parser.parse_args(args)

    print(parsed_args)

if __name__ == '__main__':
    main(sys.argv[1:])