t = int(input())
for i in range(t):
    N = int(input())
    mult_of_four = N//4
    rem = N%4
    ans = 0
    if N == 1:
        ans = 20
    elif N == 2:
        ans = 2*(6+5+4+3)
    elif  N== 3:
        ans = 2 * (6 + 5 + 4 + 3) + 6+5+4
    elif N >= 4:
        if rem == 0:
            ans = ans + 4*(6+5)*mult_of_four
            ans = ans + 4*4
        elif rem == 1:
            ans = ans + 4*(6+5)*mult_of_four
            ans = ans + 3*4
            ans = ans + (6+5+4+3)
        elif rem == 3:
            ans = ans + 4*(6+5)*mult_of_four
            ans = ans + 4
            ans = ans + 2 * (6 + 5 + 4 + 3) + 6 + 5 + 4

    print(ans)