__author__ = 'maux'

import argparse
import sys
import pandas as pd
import numpy as np
import scipy.stats as sc


def bba_ass( a ,b,max, min ):
    bba={}
    eps= 0.005
    for j in range(0,len(a)):
        p = abs (( float (max-(b[j]-min))/ float(max) ) - eps)
        theta=  1-  p
        #print b[j], a[j], p, theta
        bba[a[j]]= np.array([ p ,0, theta] )
    return bba


# # weight computation

def Dnorm(a, b):
    return (np.sum(abs(a - b)) / (0.5 * (len(a) ** 2)))


# #  BBA_combination
def BBA_comb(m_rank, bba_l, Est):
    weight = np.zeros(len(bba_l))
    for i in range(0, len(weight)):
        weight[i] = Dnorm(m_rank[:, i], Est)

    # # apply weight
    for i in range(0, n_ranker):
        O
    # #combination
    ## ready to output
    return 1


def compute_basic_estimator(flag_est, mat):
    if flag_est == 1:
        Est = sc.rankdata(np.mean(mat, axis=1))
    else:
        Est = sc.rankdata(np.median(mat, axis=1))
    return Est


def BRE_core(bba, mat_rank, n_rank, n_item, niter, flag_est):
    # # compute estimator for BRE-1T
    # median or mean
    Est = compute_basic_estimator(flag_est, mat_rank)
    c_iter = 1
    while (c_iter != niter ):
        if c_iter > 2:
            Est = compute_basic_estimator(flag_est, mat_rank)

        rep = BBA_comb(mat_rank, bba, Est)
        if c_iter == 1:
            print 'SAve Weight'
            # Mat_W[k,] <- abs(Weight)
        # replace rank
        if rep != -1:
            print 'Substitution'
            # bba[rep] = out_bba
            #mat_rank[:, rep] = out_rank
        c_iter += 1


def readFile_totRank(f):
    d=pd.read_csv(f,sep="\t",header=None)
    n_ranker= len(d.columns)-1
    n_obj= d.shape[0]
    list_rank=[]
    mat_rank= np.zeros((n_obj,n_ranker))
    for i in range(0,n_ranker):
        bba={}
        bba = bba_ass(d.ix[:,0],d.ix[:,i+1],n_obj,1)
        mat_rank[:,i]=d.ix[:,i+1].values
        print i
        list_rank.append(bba)
    return (mat_rank,list_rank,n_ranker,n_obj)


def main():
    # parse command line options
    try:
        parser = argparse.ArgumentParser(description='BRE')
        parser.add_argument('--input', dest='fileInput', action='store', help='specify ranking input file', required=True)
        parser.add_argument('--typerank', dest='flag_type', action='store', help='Type of ranking Tot.Ranking (1) or Top-k (2) ', required=True)
        parser.add_argument('--typeest', dest='flag_est', default=1,action='store', help='Type of Estimator Ranking Mean (1) or Ranking Median (2) ', required=True)
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
    flag_est=args.flag_est
    # get the data
    # print mat
    ## into BBA
    mat_rank, list_bba, n_ranker, n_item = readFile_totRank(file_name)
    # # BRE main

    BRE_core(list_bba, mat_rank, n_ranker, n_item, niter, flag_est)

if __name__ == "__main__":
    print '___'
    main()