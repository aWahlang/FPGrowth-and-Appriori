from preprocessing import parse
from helper import Itemset, genCombinations, checkItemsets, checkSubsets, checkSupport, countSupport, printResult, gen1Itemsets

def appriori (data, minSup):
    feq = {}
    feq[1] = []
    minSup = (minSup/100) * len(data)
    print("Minimum support: " + str(minSup))
    feq[1] = gen1Itemsets(data, minSup)
    k = 1
    flag = True
    while flag:
        #itemsets of size 1
        feq[k+1] = genCombinations(feq[k], k+1)
        if(len(feq[k+1]) == 0):
            flag = False
            break
        #generate subsets 
        feq[k+1] = checkSubsets(feq[k],feq[k+1],k)
        #count support
        countSupport(data, feq[k+1])
        #remove itemsets that do not meet min support
        feq[k+1] = checkSupport(feq[k+1], minSup)
        
        k += 1
    
    return feq






