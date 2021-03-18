import math
gb = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000
def res(no_of_people,egg,chocolate_bars,omelete_price,chocolate_milkshak_price,chocolate_cake_price):
    # print("egg",egg,"choclte bars",chocolate_bars,"no of people",no_of_people)
    min_price = gb

    # case 1 when only omeletes
    if (2*no_of_people) <= egg:
        # print("only omeletes")
        min_price = min(min_price,omelete_price*no_of_people)

    # case 2 only chocolate_milkshak
    if (3*no_of_people) <= chocolate_bars:
        # print("# case 2 only chocolate_milkshak")
        min_price = min(min_price,no_of_people*chocolate_milkshak_price)

    # case 3 only chocolate_cake_
    if egg >= no_of_people and chocolate_bars >= no_of_people:
        # print("# case 3 only chocolate_cake_")
        price = no_of_people*chocolate_cake_price
        min_price = min(min_price, price)
        # print("egg", egg, "choclte bars", chocolate_bars, "no of people", no_of_people)


    # case 4 omelete and milk shake
    if (egg // 2 >= 1) and (egg//2 >= (3 * no_of_people - chocolate_bars + 2) // 3):
        # print("# case 4 omelete and milk shake")
        if omelete_price < chocolate_milkshak_price:
            temp = min(no_of_people - 1, egg // 2)
        else:
            temp = max(1, (3 * no_of_people - chocolate_bars + 2) // 3)

        price = temp * (omelete_price - chocolate_milkshak_price) + no_of_people * chocolate_milkshak_price
        min_price = min(min_price, price)


    # case 5 omeltes and cakes only
    if (egg - no_of_people >= 1) and ((egg + chocolate_bars) >= 2 * no_of_people):
        # print("# case 5 omeltes and cakes only")
        if omelete_price < chocolate_cake_price:
            temp = min(no_of_people - 1, egg - no_of_people)
        else:
            temp = max(1, no_of_people - chocolate_bars)
        price = temp * (omelete_price - chocolate_cake_price) + no_of_people * chocolate_cake_price
        min_price = min(min_price, price)


    # case 6 milk shakes and cake only
    if (chocolate_bars - no_of_people)//2 >= 1 and ((chocolate_bars - no_of_people)//2 >= (no_of_people - egg)):
        # print("# case 6 milk shakes and cake only")
        if chocolate_milkshak_price < chocolate_cake_price:
            temp = min(no_of_people - 1, (chocolate_bars - no_of_people) // 2)
        else:
            temp = max(1, (no_of_people - egg))
        price = temp * (chocolate_milkshak_price - chocolate_cake_price) + no_of_people * chocolate_cake_price
        min_price = min(min_price, price)

    # case 7 omelte cake and shake
    if ((egg >= 3) and (chocolate_bars >= 4) and (no_of_people >= 3)):
        # print("all three")
        price = omelete_price + chocolate_milkshak_price + chocolate_cake_price + res(no_of_people-3,egg-3,chocolate_bars-4,omelete_price,chocolate_milkshak_price,chocolate_cake_price)
        min_price = min(min_price,price)

    return min_price
t = int(input())

for i in range(t):
    arr = [int(x) for x in input().split()]

    no_of_people = arr[0]
    egg = arr[1]
    chocolate_bars = arr[2]

    omelete_price = arr[3]
    chocolate_milkshak_price = arr[4]
    chocolate_cake_price = arr[5]
    ans = res(no_of_people,egg,chocolate_bars,omelete_price,chocolate_milkshak_price,chocolate_cake_price)
    # print(ans)
    if ans == gb:
        print(-1)
    else:
        print(ans)