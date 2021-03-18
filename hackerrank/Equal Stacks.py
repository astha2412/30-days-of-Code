

# Complete the 'equalStacks' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    sumofstack1 = sum(h1)
    sumofstack2 = sum(h2)
    sumofstack3 = sum(h3)
    print(sumofstack1,sumofstack2,sumofstack3)
    while(len(h1)!=0 and len(h2)!=0 and len(h3)!=0):
        if sumofstack1==sumofstack2 and sumofstack2==sumofstack3:
            break
        if sumofstack1>=sumofstack2 and sumofstack1>=sumofstack3:
            # print("sum of stack 1 is greatest")
            while(sumofstack1>=sumofstack2 and sumofstack1>=sumofstack3):
                dif=h1.pop(0)
                sumofstack1=sumofstack1-dif
                # print("after poping",h1)
        if sumofstack2>=sumofstack1 and sumofstack2>=sumofstack3:
            # print("h2 has max")
            while (sumofstack2>=sumofstack1 and sumofstack2>=sumofstack3):
                dif = h2.pop(0)
                sumofstack2=sumofstack2 - dif
                # print("after poping",h2)
        if sumofstack3>=sumofstack1 and sumofstack3>=sumofstack2:
            while(sumofstack3>=sumofstack1 and sumofstack3>=sumofstack2):
                dif = h3.pop(0)
                sumofstack3=sumofstack3 - dif

        print(sumofstack1,sumofstack2,sumofstack3)


    if sumofstack1 == sumofstack2 and sumofstack2 == sumofstack3:
        return sumofstack1
    elif len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
        return 0

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)
    print("results",result)
