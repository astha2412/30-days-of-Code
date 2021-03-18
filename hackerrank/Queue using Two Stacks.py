# User function Template for python3

def Push(x, stack1):
    #we just push the element at the end of 1st stack
    stack1.append(x)


def Pop(stack1, stack2):

    if len(stack1) == 0 and len(stack2) == 0:
        #empty
        return -1
    elif len(stack2)==0:
        # copy all values to stack 1 to stack 2 and then pop
        while(len(stack1)!=0):
            pi = stack1.pop()
            stack2.append(pi)
        stack2.pop()
    else:
        stack2.pop()

def display(stack1,stack2):
    if len(stack1) == 0 and len(stack2) == 0:
        #empty
        return -1
    elif len(stack2)==0:
        # copy all values to stack 1 to stack 2 and then pop
        while(len(stack1)!=0):
            pi = stack1.pop()
            stack2.append(pi)
        pi=stack2.pop()
    else:
        pi=stack2.pop()
    print(pi)
    stack2.append(pi)

if __name__ == '__main__':
    i = 0
    stack1 = []
    stack2 = []
    test_cases = int(input())
    # test_cases = 1
    for cases in range(test_cases):
        qtyp_qry = list(map(int, input().strip().split()))
        # print(i)
        if qtyp_qry[0] == 1:
            Push(qtyp_qry[1], stack1)
            # print("pushed")
            i += 2
        elif qtyp_qry[0] == 2:
            # print("poped")
            Pop(stack1,stack2)
            i += 1
        elif qtyp_qry[0] == 3:
            display(stack1,stack2)
        # print(stack1,stack2)

# } Driver Code Ends