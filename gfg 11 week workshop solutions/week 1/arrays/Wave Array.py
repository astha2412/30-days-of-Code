# User function Template for python3


class Solution:

    def reverseInGroups(self, arr, N, K):
        arr1 = []
        if K >= N:
            arr1 = arr
            arr1.reverse()
            arr[:] = arr1

        else:
            arr1 = []
            for i in range(0, N, K):
                # print(i)
                lst = arr[i:i + K]
                lst.reverse()
                # print(lst)
                for i in lst:
                    arr1.append(i)
            # print(arr1)
            arr[:] = arr1

    def convertToWave(self, A, N):
        lst = self.reverseInGroups(A, N, 2)
        # print(lst)
        return lst


import math

# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().split()]
        ob = Solution()
        ob.convertToWave(A, N)
        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends