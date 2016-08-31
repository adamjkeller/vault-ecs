from argparse import ArgumentParser

class GetArgs(object):

    def get_args(self):
        parser = ArgumentParser()
        parser.add_argument('-t', '--token', action='store', dest='token', help='Token', type=str, required=True)
        parser.add_argument('-k1', '--key1', action='store', dest='key1', help='First Unseal Key', type=str, required=True)
        parser.add_argument('-k2', '--key2', action='store', dest='key2', help='First Unseal Key', type=str, required=True)
        parser.add_argument('-k3', '--key3', action='store', dest='key3', help='First Unseal Key', type=str, required=True)
        return parser.parse_args()

if __name__ == '__main__':
    args = GetArgs()
    print args.get_args()
