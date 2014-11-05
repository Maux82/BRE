__author__ = 'maux'

import argparse
import sys



def main():
    # parse command line options
    try:
        parser = argparse.ArgumentParser(description='BRE')
        parser.add_argument('--input', dest='name', action='store', help='specify input list of MS2 peptides ', required=True)
        args = parser.parse_args()


    except parser.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options

    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

if __name__ == "__main__":
    print ''
    main()