# cook your dish here
def maxDiff(arr, n):
    # Initialize Result
    maxDiff = -1

    # Initialize max element from
    # right side
    maxRight = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if (arr[i] > maxRight):
            maxRight = arr[i]
        else:
            diff = maxRight - arr[i]
            if (diff > maxDiff):
                maxDiff = diff
    return maxDiff
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()];
        n = len(arr);
        print(maxDiff(arr,n))
