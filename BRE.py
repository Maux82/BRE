__author__ = 'maux'

import argparse
import sys
import pandas as pd
import numpy as np

def bba_ass( a ,b,max, min ):
    bba={}
    for j in range(0,len(a)):
        p= ((max-(b[j]-min))/max )
        theta=  1-p
        bba[a[j]]= np.array([ p ,0, theta] )
    return bba

##

def readFile_totRank(f):
    d=pd.read_csv(f,sep="\t")
    n_ranker= len(d.columns)-1
    n_obj= d.shape[0]
    list_rank=[]
    for i in range(1,n_ranker):
        bba={}
        bba = bba_ass(d.ix[:,0],d.ix[:,i],n_obj,1)
        print bba
        list_rank.append(bba)
    return (list_rank,n_ranker,n_obj)
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
    print readFile_totRank(file_name)
    ## into BBA
    ## BRE main loop
if __name__ == "__main__":
    print '___'
    main()