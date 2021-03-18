# User function Template for python3


'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def printLevelOrder(root1):
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
        print(current_pounter.data, end=" ")
        queue.pop(0)

    return
def rightView(root1):
    print("right view")
    res = []
    if root1==None:
        res.append(-1)
        return res
    queue = []
    queue.append(root1)
    # delimeter
    queue.append(None)
    while(len(queue)!=0):
        current_pounter = queue[0]
        if current_pounter!=None:
            while(queue[0]!=None):
                if current_pounter.left!=None:
                    queue.append(current_pounter.left)
                if current_pounter.right!=None:
                    queue.append(current_pounter.right)

                lastnode=queue.pop(0)
                current_pounter=queue[0]
            # print(lastnode.data,end=" ")
            res.append(lastnode.data)
            queue.append(None)
        queue.pop(0)

    return res

def leftView(root1):
    print("left view")
    res = []
    if root1==None:
        res.append(-1)
        return res
    queue = []
    queue.append(root1)
    # delimeter
    queue.append(None)
    while(len(queue)!=0):
        current_pounter = queue[0]
        if current_pounter!=None:
            # print(current_pounter.data,end=" ")
            res.append(current_pounter.data)
            while(queue[0]!=None):
                if current_pounter.left!=None:
                    queue.append(current_pounter.left)
                if current_pounter.right!=None:
                    queue.append(current_pounter.right)

                queue.pop(0)
                current_pounter=queue[0]
            queue.append(None)
        queue.pop(0)

    return res

from collections import deque
import queue


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
    # t = int(input())
    t=1
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        result = leftView(root)
        print(result)
        for value in result:
            print(value, end=" ")
        print()
        result = rightView(root)
        print(result)
        for value in result:
            print(value, end=" ")
        print()

# } Driver Code Ends