
def twoStacks(x, a, b):
    stack = []
    print(a,b)
    pi=0
    sum1=0
    while(len(a)!=0 and len(b)!=0):
        if a[0]<= b[0]:
            pi = a.pop(0)
        elif b[0]<a[0]:
            pi = b.pop(0)
        else:
            print(-1)
        stack.append(pi)
        sum1=sum1+pi
        if sum1<=x:
            pass
        else:
            sum1=sum1-pi
            stack.pop()
            break
    if (len(a) == 0 or len(b) ==0) and sum1<x:
        if len(a) == 0 and len(b)!=0:
            while(len(b)!=0):
                pi = b.pop(0)
                sum1 = sum1+pi
                stack.append(pi)
                if sum1>x:
                    stack.pop()
                    sum1=sum1-pi
                    break
                else:
                    pass
        elif len(a) == 0 and len(b)!=0:
            while(len(b)!=0):
                pi = a.pop(0)
                sum1 = sum1+pi
                stack.append(pi)
                if sum1>x:
                    stack.pop()
                    sum1=sum1-pi
                    break
                else:
                    pass
        else:
            pass
    print(stack,pi,sum1,a,b)
    return len(stack)

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)
        print(result)