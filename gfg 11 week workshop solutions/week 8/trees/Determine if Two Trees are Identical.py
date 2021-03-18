# User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


# your task is to complete this function
# function should return true/false or 1/0
def printLevelOrder(root1):
    res=[]
    if root1==None:
        return
    queue = []
    queue.append(root1)
    while(len(queue)!=0):
        current_pounter = queue[0]

        if current_pounter.left!=None:
            queue.append(current_pounter.left)
        if current_pounter.right!=None:
            queue.append(current_pounter.right)
        # print(current_pounter.val, end=" ")
        res.append(current_pounter.data)
        queue.pop(0)

    return res
def isIdentical(root1, root2):
    res1=printLevelOrder(root1)
    res2=printLevelOrder(root2)
    # print(res2,res1)
    if res1==res2:
        return True
    else:
        return False

# Initial Template for Python 3


# Contributed by Sudarshan Sharma
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s1 = input()
        s2 = input()
        head1 = buildTree(s1)
        head2 = buildTree(s2)
        if isIdentical(head1, head2):
            print("Yes")
        else:
            print("No")

# } Driver Code Ends