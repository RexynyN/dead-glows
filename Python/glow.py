from primes import primes_primes_more_primes
from idiotifier import idiotify
from math import sqrt
import argparse
from os import getcwd

# sub-command functions
def foo(args):
    print(args)

def bar(args):
    print('((%s))' % args.z)

try:
    # Create the top-level parser
    parser = argparse.ArgumentParser(description="A multiplatform toolbox for everything you need", prog="glow")
    parser.add_argument("action", type=str, help="You need to say what you want. Glow is magical, but can't read minds you know...")
    subparsers = parser.add_subparsers()

    # Create the parser for the "primes" command
    prime_parser = subparsers.add_parser("primes")
    prime_parser.add_argument("threshold", type=int, default=1000, help="Number of primes to return")
    prime_parser.set_defaults(func=primes_primes_more_primes)

    # Create the parser for the "idiotifier" command
    filerename_parser = subparsers.add_parser('idiotifier')
    filerename_parser.add_argument('text', type=str, help="The text to idiotify")
    filerename_parser.set_defaults(func=idiotify)

    # create the parser for the "bar" command
    parser_bar = subparsers.add_parser('bar')
    parser_bar.add_argument('z')
    parser_bar.set_defaults(func=bar)

    # parse the args and call whatever function was selected
    args = parser.parse_args()
    args.func(args)
except Exception as e:
    print("Something went terrible wrong, we're sorry. Try again")
    print("If you understand what it means, this is what happened: " + e.__cause__)