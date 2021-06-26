# 18 4 16 8 23 13 20 11 28 24 26 25 1 30 15 19
def merge_row(index, arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = []
    R = []
    for i in range(n1):
        L.append(arr[index][l + i])
    for i in range(n2):
        R.append(arr[index][m+1+i])
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[index][k] = L[i]
            i += 1
        else:
            arr[index][k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[index][k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[index][k] = R[j]
        j += 1
        k += 1

def merge_column(index, arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = []
    R = []
    for i in range(n1):
        L.append(arr[l+i][index])
    for i in range(n2):
        R.append(arr[m+1+i][index])
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k][index] = L[i]
            i += 1
        else:
            arr[k][index] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k][index] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k][index] = R[j]
        j += 1
        k += 1

def merge_sort(arr, start_row, start_column, end_row, end_column):
    if start_row >= end_row and start_column >= end_column:
        return
    mid_row = start_row + (end_row - start_row) // 2
    mid_column = start_column + (end_column - start_column) // 2
    merge_sort(arr, start_row, start_column, mid_row, mid_column)
    merge_sort(arr, start_row, mid_column+1, mid_row, end_column)
    merge_sort(arr, mid_row+1, start_column, end_row, mid_column)
    merge_sort(arr, mid_row+1, mid_column+1, end_row, end_column)
    for i in range(start_row, end_row+1):
        merge_row(i, arr, start_column, mid_column, end_column)
    for i in range(start_column, end_column+1):
        merge_column(i, arr, start_row, mid_row, end_row)
x, y = map(int, input().split(' '))
arr2 = [int(i) for i in input().split()]
arr2 = arr2[::-1]
# print(arr2)
arr = []
for i in range(x):
    arr.append([])
    for j in range(y):
        a = arr2.pop()
        arr[i].append(a)
merge_sort(arr, 0, 0, x-1, y-1)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")