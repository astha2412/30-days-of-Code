# User function Template for python3

def subArraySum(arr, n, sum):
    # Your code here
    cursum = arr[0]
    l = 0
    lst = []
    for i in range(1, n):
        cursum = cursum + arr[i]
        # print(cursum)
        if cursum > sum:
            cursum = cursum - arr[l]
            l = l + 1
        if cursum == sum:
            # print(l + 1, i + 1)
            lst.append(l+1)
            lst.append(i+1)
            return lst
    else:
        # print(-1)
        lst.append(-1)
        return lst


# {
#  Driver Code Starts
# Initial Template for Python 3

import math




if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))

        ans=subArraySum(A, N, S)
        for i in ans:
            print(i,end=" ")
        print()

        T -= 1
# } Driver Code Ends