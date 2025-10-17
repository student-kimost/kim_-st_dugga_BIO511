#Writen by Kim Öst
#BIO511

import csv
import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', help = 'Specify a csv file')

args=parser.parse_args()

df = pd.read_csv(args.filename)

def plott_histogram():
    plt.hist(df['fpkm_log2'])
    plt.xlabel('Expression')
    plt.ylabel('Number of genes')
    plt.title('Distrubution of gene expression')
    plt.savefig('fpkm_distribution.png',dpi=300)


plott_histogram()
