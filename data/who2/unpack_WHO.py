
import sys,os
import pandas as pd

WHO  = pd.read_csv('1673403181.61834_whodonreports.csv')

for i in range(1,len(WHO)):
    dirname = '%04d' % i
    os.mkdir(dirname)
    for k in WHO.keys():
        with open(dirname + '/' + k, 'w') as fd:
            print(WHO[k][i], file=fd)
