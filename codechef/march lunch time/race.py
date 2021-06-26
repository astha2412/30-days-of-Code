'''
Ann is going to take part in a race. At the start, she has X units of energy. For each subsequent second, she can decide to run or to rest (she must perform the chosen action during the whole second). If she runs, she loses one unit of energy during that second and if she rests, she gains one unit of energy during that second. However, if Ann decides to rest when she has X units of energy, she does not gain any extra energy. Naturally, she cannot decide to run if she has 0 units of energy.
Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains three space-separated integers X, R and M.
Output
For each test case, print a single line containing the string "YES" if Ann is able to finish the race or "NO" otherwise (without quotes).

Constraints
1≤T≤105
1≤X,R,M≤109
Subtasks
Subtask #1 (100 points): original constraints

Example Input
2
60 3 5
60 3 4
Example Output
YES
NO
'''
import math
t=int(input())
for i in range(t):
    lst = [int(x) for x in input().split()]
    X = lst[0]
    R = lst[1]
    M = lst[2]
    if X<=0:
        print("NO")
    elif math.ceil(M/2)>=R:
        print("YES")
    else:
        print("NO")