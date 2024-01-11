import argparse

def args_parser():
    parser = argparse.ArgumentParser()

    # encrypt or decrypt
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', help='encrypt a message', action='store_true')
    group.add_argument('-d', '--decrypt', help='decrypt a message', action='store_true')

    return parser.parse_args()

if __name__ == '__main__':
    args = args_parser()