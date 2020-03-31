import argparse

from caesar_encryption import encrypt


def caesar():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('text', nargs='*')
    parser.add_argument('-k', '--key', type=int, default=1, metavar='1..25', choices=range(1,26), help="pass a number between 1 to 25")
    args = parser.parse_args()

    text_string = ' '.join(args.text)
    key = args.key
    if args.decrypt:
        key = -key
    cyphertext = encrypt(text_string, key)
    print(cyphertext)

if __name__ == '__main__':
    caesar()