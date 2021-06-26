# Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an array A: 
def equilibriumPoint(arr, N):
    # finding the sum of whole array
    total_sum = sum(arr)
    leftsum = 0
    if N == 1:
        return 1
    for i, num in enumerate(arr):

        # total_sum is now right sum
        # for index i
        total_sum -= num

        if leftsum == total_sum:
            return i + 1
        leftsum += num

        # If no equilibrium index found,
    # then return -1
    return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        print(equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends