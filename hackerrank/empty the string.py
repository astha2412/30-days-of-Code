# User function Template for python3

class Solution:
    def makeStringEmpty(self, s):
        sub_str = 'geek'
        l=10
        count = 0
        while(l>0):
            find = s.find(sub_str)
            if find == -1:
                pass
            else:
                # print("before",s)
                s=s[0:find]+s[find+4:]
                # print("after",s)
                count+=1

            l-=1
        if len(s) == 0:
            return count
        else:
            return -1


# {
#  Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.

if __name__ == '__main__':
    # t = int(input())
    t=1
    for _ in range(t):
        s = input()
        # s="gegeekek"
        ob = Solution()
        print(ob.makeStringEmpty(s))
# } Driver Code Ends