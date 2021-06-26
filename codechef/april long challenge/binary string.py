def decimalToBinary(n):
    return bin(n).replace("0b", "")


def isSubSequence(str1, str2):
    m = len(str1)
    n = len(str2)

    j = 0  # Index of str1
    i = 0  # Index of str2

    while j < m and i < n:
        if str1[j] == str2[i]:
            j = j + 1
        i = i + 1

    # If all characters of str1 matched,
    # then j is equal to m
    return j == m
t = int(input())
for i in range(t):
    str1 = input()
    i=0
    while(True):
        str2 = decimalToBinary(i)
        res = isSubSequence(str2,str1)
        # print(i,res)
        if res == True:
            pass
        else:
            print(str2)
            break
        i=i+1

