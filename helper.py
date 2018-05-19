import itertools

class Itemset:
    support = 0
    items = []

    def __init__(self, i = '',s = 0):
        self.items = [i]
        self.support = s



def gen1Itemsets(data, minSup):
    feq = []
    #frequent itemsets of size 1
    for key in data:
        for value in data[key]:
            index = checkItemsets(feq, value)
            if( index != None):
                feq[index].support += 1
            else:
                x = Itemset(value, 1)
                feq.append(x)
    
    feq = checkSupport(feq, minSup)
    return feq


def genCombinations (l,size):
    can = []
    combi = []
    for itemset in l:
        for value in itemset.items:
            if(value not in combi):
                combi.append(value)

    combi = list(itertools.combinations(combi,size))
    for i in range (0, len(combi)):
        x = Itemset()
        x.items = list(combi[i])
        can.append(x)

    return can

def checkItemsets(l, item):
    for value in l:
        if(item in value.items):
            return l.index(value)
    
    return None

def checkSupport (l, supp):
    i = 0
    while i < len(l):
        if(l[i].support < supp ):
            x = l.index(l[i])
            del l[i]
            i -= 1
        i += 1
    return l

def printResult(dic):
    for key in dic:
        if(len(dic[key]) == 0):
            return
        print("\nFrequent Itemset size: "+str(key) +"\n")
        for itemset in dic[key]:
            print(itemset.items, end = "", flush = True)
            print(" SUPPORT: " + str(itemset.support))

def checkSubsets (f,l,size):
    check = []
    i = 0
    for itemset in f:
        check.append(itemset.items)
    while i < len(l):
        subsets = []
        subsets = list(itertools.combinations(l[i].items,size))
        for j in range (0, len(subsets)):
            if(list(subsets[j]) not in check):
                del l[i]
                i -= 1
                break
        
        i += 1
    return l

def countSupport(data,l):
    for itemset in l:
        for key in data:
                if(set(itemset.items).issubset(data[key])):
                    itemset.support += 1
    return l
