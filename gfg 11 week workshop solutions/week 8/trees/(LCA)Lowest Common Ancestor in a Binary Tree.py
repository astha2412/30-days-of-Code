# User function Template for python3

'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''


# If LCA exist, return reference to it. If
# If both n1 and n2 are not present,
# rturn None. Else if left subtree contains any
#  of them return pointer to left.
def find_Path(root1,path,k):
    if root1 == None:
        return False
    path.append(root1.data)
    if root1.data == k:
        return True
    if ((root1.left and find_Path(root1.left,path,k)) or (root1.right and find_Path(root1.right,path,k))):
        return True
    path.pop()
    return False

def lca(root, n1, n2):
    path1 = []
    path2 = []
    if ((not find_Path(root,path1,n1)) or (not find_Path(root,path2,n2))):
        return -1

    # to store paths to n1 and n2 from the root
    #
    # // Find paths from root to n1 and root to n1.
    # // If either n1 or n2 is not present, return -1
    #
    # // Compare the paths to get the first
    # // different value
    i=0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i+=1

    val = path1[i-1]
    tmp = Node(val)
    return tmp

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
        a, b = list(map(int, input().split()))
        s = input()
        root = buildTree(s)
        k = lca(root, a, b)
        print(k.data)

# } Driver Code Ends