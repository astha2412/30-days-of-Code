def binaryToDecimal(n):
    return int(n,2)
from itertools import combinations
import itertools
def decimalToBinary(n):
    return bin(n).replace("0b", "")
def subString(x):
    lst=[''.join(l) for i in range(len(x)) for l in combinations(x, i + 1)]
    return lst

def Sub_Sequences(STR):
    combs = []
    lst=[]
    for l in range(1, len(STR)+1):
        combs.append(list(itertools.combinations(STR, l)))
    for c in combs:
        for t in c:
            a=''.join(t)
            lst.append(a)
    return lst

t = int(input())
for i in range(t):
    str1 = input()
    lst = subString(str1)
    lst3 = Sub_Sequences(str1)
    # print(lst3)
    lst2 = []
    for i in lst3:
        lst2.append(binaryToDecimal(i))
    lst2.sort()
    lst2 = list(set(lst2))
    # print(lst2)
    hashmap = {}
    for i in lst2:
        if i in hashmap.keys():
            pass
        else:
            hashmap[i] = True
    # print(hashmap)
    i=0
    while(True):
        try:
            if hashmap[i] == True:
                pass
            else:
                break
        except:
            break
        i=i+1
    print(decimalToBinary(i))
