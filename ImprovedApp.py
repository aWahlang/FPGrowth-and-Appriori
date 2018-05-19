import copy
from app import appriori
from helper import countSupport

def checkfeq(l,f,n):
    for item in f[n]:
        if(set(l) == set(item.items)):
            return True
    return False

def PartitionedApp (data, min):
    dataKeys = list(data.keys())
    split = int(len(dataKeys)/4)
    feq = {}

    for i in range(0,4):
        #partitioning the dataset
        index = dataKeys[i*split:(i+1)*split]
        part = {k:data[k] for k in index}
        subFeq = appriori(part,min)
        for key in subFeq:
            if(key not in feq.keys()):
                feq[key] = []
            #combining result frequent itemsets
            for item in subFeq[key]:
                if(checkfeq(item.items,feq,key) ==  False):
                    temp = copy.deepcopy(item)
                    temp.support = 0
                    feq[key].append(temp)
    #counting true support
    for key in feq:
        feq[key] = countSupport(data,feq[key])

    return feq



