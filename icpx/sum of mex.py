def MEX(lst):
    # lst = [1,0]
    lst.sort()
    print(lst)
    if len(lst) <=2 :
        if 0 not in lst:
            return 0
        elif 1 not in lst:
            return 1
        elif 2 not in lst:
            return 2
        else:
            pass
    for i in range(len(lst)-1):
        if i in lst:
            pass
        else:
            return i
        if lst[i+1] - lst[i] == 1 or lst[i+1] == lst[i]:
            print(lst[i+1],lst[i])
        else:
            return lst[i]+1
    print("last",lst[-1])
    return lst[-1]+1

# print("MEX is",MEX())
t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    sum1=0
    for i in arr:
        sum1 = sum1 + MEX(i)

    print(sum1)
