__author__ = 'maux'

import argparse
import sys

def

def main():
    # parse command line options
    try:
        parser = argparse.ArgumentParser(description='BRE')
        parser.add_argument('--input', dest='fileInput', action='store', help='specify ranking input file', required=True)
        parser.add_argument('--typerank', dest='flag_type', action='store', help='Type of ranking Tot.Ranking (1) or Top-k (2) ', required=True)
        parser.add_argument('--niter', dest='niter',default=1 ,action='store', help='number of Bre iteration > 0. default BRE-1T', required=True)

        args = parser.parse_args()


    except parser.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options

    file_name= args.fileInput
    flag_type= args.flag_type
    niter =args.niter
    # get the data
    ## into BBA
    ## BRE main loop
if __name__ == "__main__":
    print '___'
    main()