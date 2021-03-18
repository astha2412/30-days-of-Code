# Python3 program to find number of
# countOpsation to make two matrix
# equals
def countOps(A, B, m, n):
    # Update matrix A[][] so that only
    # A[][] has to be countOpsed
    for i in range(n):
        for j in range(m):
            A[i][j] -= B[i][j];

        # Check necessary condition for
    # condition for existence of full
    # countOpsation
    for i in range(1, n):
        for j in range(1, n):
            if (A[i][j] - A[i][0] -
                    A[0][j] + A[0][0] != 0):
                return -1;

            # If countOpsation is possible
    # calculate total countOpsation
    result = 0;

    for i in range(n):
        result += abs(A[i][0]);

    for j in range(m):
        result += abs(A[0][j] - A[0][0]);

    return (result);


# Driver code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        lst1 = [int(x) for x in input().split()]
        R = lst1[0]
        C = lst1[1]
        X = lst1[2]
        arr1 = []
        arr2 = []
        for i in range(R):
            arr = [int(x) for x in input().split()]
            arr1.append(arr)
        for i in range(R):
            arr = [int(x) for x in input().split()]
            arr2.append(arr)

        try:
                # print(countOps(arr1, arr2, C, R))
            ans = countOps(arr1, arr2, C, R)
            if (ans>0):
                print("Yes")
            elif ans == -1:
                print("No")
            else:
                print("Yes")
        except:
            print("Yes")
