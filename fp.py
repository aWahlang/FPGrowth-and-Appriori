import copy
import itertools
from preprocessing import parse, discretize
from helper import gen1Itemsets, Itemset, printResult

class Node:
    item = ''
    count = 0
    children = []

    def __init__(self, i = '', c = 0):
        self.item = i
        self.count = c

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.item)+repr(' count:')+repr(self.count)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

def show(l):
    for itemset in l:
        print(itemset.items)
        print("Support: " + str(itemset.support))

def showTree(fp):
    print(fp.item + " Count: "+ str(fp.count))
    if(len(fp.children) == 0):
        print("----------------------end of branch---------------------")
        return
    else:
        for child in fp.children:
            showTree(child) 


def itemset2list(l):

    x = []
    for itemset in l:
        for value in itemset.items:
            x.append(value)
    return x

def getOrderedfeq(d,h):

    c = []
    for item in h:
        if(item in d):
            c.append(item)
    return c

def buildTree(node, l):
    found = False
    if (len(l) == 0):
        return
    if(len(node.children) > 0):
        for child in node.children:
            if(child.item == l[0]):
                child.count += 1
                del l[0]
                buildTree(child, l)
                found = True
                break
        if(not found):
            new = Node(l[0],1)
            t = [new]
            node.children = node.children + t
            del l[0]
            buildTree(node.children[len(node.children) - 1], l)
    else:
        n = Node(l[0], 1)
        temp = [n]
        node.children = node.children + temp
        del l[0]
        buildTree(node.children[0],l)


def getCPB(rt, val, path, store):
    if(rt.item != ''):
        path.append(rt.item)
    if(rt.item == val):
        temp = copy.deepcopy(path)
        i = Itemset()
        i.items = temp
        i.support = rt.count
        store.append(i)
        path.pop()
        return

    elif(rt.children == []):
        path.pop()
        return

    else:
        for child in rt.children:
            getCPB(child, val, path, store)
        if(path != []):
            path.pop()
        return


def getSupCPB(s,l):
    sup = 0
    for item in l:
        if(set(s).issubset(item.items)):
            sup += item.support
    return sup

def checkfeq(l,f,n):
    for item in f[n]:
        if(set(l) == set(item.items)):
            return True
    return False

def CPB2FPB (dic, minSup, feq):
    for key in dic:
        for item in dic[key]:
            for i in range(2, len(item.items)+1):
                combo = list(itertools.combinations(item.items, i))
                for x in combo:
                    x = list(x)
                    s = getSupCPB(x, dic[key])
                    if(s > minSup):
                        if(i not in feq.keys()):
                            feq[i] = []
                        if(checkfeq(x,feq,i) == False):
                            new = Itemset()
                            new.items = copy.deepcopy(x)
                            new.support = s
                            feq[i].append(new)
    
    return


def FPGrowth(data, min):
    minSup = (min/100) * len(data)
    print("Minimum support: " + str(minSup))
    
    root = Node()
    CPB = {}
    feq = {}
    cpStore = []
    feq[1] =[]
    # itemsets of size 1
    feq[1] = gen1Itemsets(data, minSup)
    feq[1].sort(key = lambda c: c.support, reverse = True)
    header = itemset2list(feq[1])
    #building FP tree
    def FPtree (data, rt, head):
        for key in data:
            itemlist = getOrderedfeq(data[key],head)
            buildTree (rt, itemlist)

    FPtree(data,root,header)
    #building Conditional Pattern Base
    for item in header:
        getCPB(root, item, [],cpStore)
        CPB[item] = copy.deepcopy(cpStore)
        cpStore = []

    del CPB[header[0]]
    #Generating frequetn itemeset form Conditonal Pattern Base
    CPB2FPB(CPB,minSup, feq)
    print("FP TREE : \n")
    print(root)
    return feq














