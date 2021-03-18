'''
S = ""
1 append(W) - Append string W  to the end of S.
2 delete(k) - Delete the last  characters of S.
3 print(k) - Print the kth character of S.
4 undo - Undo the last (not previously undone) operation of type  or , reverting  to the state it was in prior to that operation.
'''

#time limit is exceding
S=""
stack = []
# q=int(input())
# for i in range(q):
while(True):
    lst = [x for x in input().split()]
    typeofquery = int(lst[0])
    # print(lst)
    if typeofquery == 4:
        pass
    else:
        try:
            # print(typeofquery)
            opr = lst[1]
        except:
            print("query is",typeofquery)


    if typeofquery == 1:
        print("appending new str")
        S = S + opr
        print(S)
        stack.append(S)
        print(S, stack)
    elif typeofquery == 2:
        print("deleting last",opr," chars from",S)
        opr = int(opr)
        S = S[0:len(S)-opr]
        print("after deleting string is",S)
        stack.append(S)
        print(S, stack)
    elif typeofquery == 3:
        opr = int(opr)
        print("display S")
        try:
            print(S[opr-1])
        except:
            print("string display nahi ho pa ra hai",opr)
    elif typeofquery == 4:
        # print("current string is",S,stack)
        try:
            stack.pop()
            S = stack.pop()
            stack.append(S)
        except:
            S=""
            stack.append("")
            print("except",stack,S)
        # print("after undo",S)

        print(stack)

