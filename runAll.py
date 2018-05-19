import time
import pandas as pd
from preprocessing import parse
from app import appriori
from helper import printResult
from fp import FPGrowth
from ImprovedApp import PartitionedApp

start = time.time()
df = pd.read_csv('adult.data.csv', names=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
dataSet= parse(df, df.shape[0])
sec = time.time() - start
print("\nData Preprocessing time: " + str(sec)+" seconds")
minSup = int(input("Enter minimun relative support as a percentage (0 - 100) : "))
print('\n--------------------------------- APRIORI --------------------------------------')
#
#start = time.time()
#feqApp = appriori(dataSet,minSup)
#printResult(feqApp)
#sec = time.time() - start
#print("\nApriori Execution time: " + str(sec)+" seconds")
#print('\n--------------------------------- FP GROWTH --------------------------------------')

start = time.time()
feqFP = FPGrowth(dataSet,minSup)
printResult(feqFP)
sec = time.time() - start
print("\nFP Growth Execution time: " + str(sec)+" seconds")
print('\n--------------------------------- PARTITIONED APRIORI --------------------------------')

#start = time.time()
#feqPApp = PartitionedApp(dataSet, minSup)
#printResult(feqPApp)
#sec = time.time() - start
#print("\nPartitioned Apriori Execution time: " + str(sec)+" seconds")