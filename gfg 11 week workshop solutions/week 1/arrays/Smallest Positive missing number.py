#User function Template for python3

def findMissing(arr, size):
    # your code goes here
    for i in range(1,size+1):
        if i in arr:
            # print(i)
            pass
        else:
            return i

def findMissing2(arr,size):
    hash_map={}
    for i in arr:
        hash_map[i]=1
    # print(hash_map)
    for i in range(1,size+1):
        try:

            if hash_map[i] == 1:
                pass
            else:
                return i
        except:
            return i
    return size+1
#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(findMissing2(arr, n))
# } Driver Code Ends