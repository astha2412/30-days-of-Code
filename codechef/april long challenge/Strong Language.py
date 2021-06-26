'''
A string is said to be using strong language if it contains at least K consecutive characters '*'.

You are given a string S with length N. Determine whether it uses strong language or not.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains a single string S with length N.
Output
Print a single line containing the string "YES" if the string contains strong language or "NO" if it does not (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Constraints
1≤T≤10
1≤K≤N≤106
S contains only lowercase English letters and characters '*'
Sum of N over all testcases is atmost 106.
Subtasks
Subtask #1 (30 points): N≤104, Sum of N over all testcases is atmost 104
Subtask #2 (70 points): original constraints

Example Input
3
5 2
*a*b*
5 2
*a**b
5 1
abcde
Example Output
NO
YES
NO
'''
t = int(input())
for i in range(t):
    arr = [float(x) for x in input().split()]
    N = arr[0]
    K = arr[1]
    str1 = input()
    max1 = 0
    c=0
    for i in str1:
        if i == '*':
            c=c+1
            # print(c)
        else:
            c=0
        if c>=max1:
            max1=c
    # print(max1)
    if max1 >= K:
        print("YES")
    else:
        print("NO")
