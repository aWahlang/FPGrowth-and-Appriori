import pandas as pd
def discretize(l):
    
    age = l[0]
    if(age < 18):    
        age = 'child'
    elif(age >= 18 and age <= 29):
        age = 'young-adult'
    elif(age >= 30 and age <= 45):
        age = 'adult'
    elif(age >= 45 and age <= 60):
        age = 'middel-aged'
    elif(age >= 60):
        age = 'senior'
    l[0] = age

    hrs = l[12]
    if(hrs < 10):
        hrs = '<10'
    elif(hrs >= 10 and hrs < 20):
        hrs = '10-20'
    elif(hrs >= 20 and hrs < 30):
        hrs = '20-30'
    elif(hrs >= 30 and hrs < 40):
        hrs = '30-40'
    elif(hrs >= 40 and hrs < 50):
        hrs = '40-50'
    elif(hrs >= 50 and hrs < 60):
        hrs = '50-60'
    elif(hrs >= 60 and hrs < 70):
        hrs = '60-70'
    elif(hrs >= 70):
        hrs = '>70'
    l[12] = hrs    

    gain = l[10]
    if(gain <= 5000):
        gain = "low-gain"
    elif(gain > 5000 and gain <=50000):
        gain = "medium-gain"
    elif(gain > 50000):
        gain = "high-gain"
    l[10] = gain

    loss = l[11]
    if(loss <= 5000):
        loss = "low-loss"
    elif(loss > 5000 and loss <=50000):
        loss = "medium-loss"
    elif(loss > 50000):
        loss = "high-loss"
    l[11] = loss


    del l[2]
    del l[3]

    for i in range(0,13):
        l[i] = l[i].strip()
        
    return l


def parse(df,n):
    data = {}
    j = 0
    for i in range(0,n):
        tup = list(df.loc[i])
        if(' ?' not in tup):
            data[j] = discretize(tup)
            j += 1

    return data