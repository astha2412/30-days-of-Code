def highlow(lst):
    flag = True
    if lst[1] > lst[0]:
        # ith is gratr than i-1
        for i in range(1, len(lst)):
            if i % 2 == 0:
                # even index
                if lst[i] < lst[i - 1]:
                    pass
                else:
                    flag = False
                    break
            else:
                # odd index
                if lst[i] > lst[i - 1]:
                    pass
                else:
                    flag = False
                    break

    else:

        for i in range(1, len(lst)):
            if i % 2 == 0:
                # even index
                if lst[i] > lst[i - 1]:
                    pass
                else:
                    flag = False
                    break
            else:
                # odd index
                if lst[i] < lst[i - 1]:
                    pass
                else:
                    flag = False
                    break

    if flag == True:
        return True
    else:
        return False

print(highlow( [3, 2, 3, 1, 3, 2] ))