import argparse
import algo

def args_parser():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt messages using various algorithm.')

    # encrypt or decrypt
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', help='encrypt a message', action='store_true')
    group.add_argument('-d', '--decrypt', help='decrypt a message', action='store_true')

    # algorithm
    parser.add_argument('-a', '--algorithm', help='the algorithm to use', required=True)

    # key
    parser.add_argument('-k', '--key', help='the key to use to encrypt or decrypt', required=True)

    # message
    parser.add_argument('message', help='the message to encrypt or decrypt')

    return parser.parse_args()

if __name__ == '__main__':
    args = args_parser()

    try:
        exec('print(algo.{}.run(args.message, args.key, args.encrypt))'.format(args.algorithm.lower()))
    except AttributeError:
        print('{} algorithm is invalid or not yet implemented.'.format(args.algorithm))

    print(args)