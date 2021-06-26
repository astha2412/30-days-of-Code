t = int(input())
for i in range(t):
    lst1 = [int(x) for x in input().split()]
    n = lst1[0]
    m=lst1[1]
    k = lst1[2]
    lst2 = [int(x) for x in input().split()]
    if m>=n:
        print("YES")
    else:
        lst2.sort()
        mth_smallest = lst2[m]
        print(mth_smallest)
        if lst2[1]>mth_smallest:
            print("NO")
        elif lst2[1]<=mth_smallest:
            print("YES")
        else:
            print("may be")
