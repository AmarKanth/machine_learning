"""
1) Count the even sum of subsets in the given array
"""
def count_even_sum_subsets(arr):
    MOD = 10**9 + 7
    n = len(arr)
    f = False

    for x in arr:
        if x % 2 == 1:
            f = True
            break

    exp = n-1 if f else n
    return pow(2, exp, MOD)-1

res = count_even_sum_subsets([2,4,6,1])
print(res)


"""
2) There are N cards on the table and each has a number between 0 and N. 
Let us denote the number on the ith card by ci. 
You want to pick up all the cards. The ith card can be picked up only if 
at least ci cards have been picked up before it. (As an example, if a card has a 
value of 3 on it, you can't pick that card up unless you've already picked up 
3 cards previously) In how many ways can all the cards be picked up?
"""
def ways_to_pick_cards(cards):
    MOD = 10**9 + 7
    n = len(cards)
    sorted_cards = sorted(cards)
    res = 1

    if sorted_cards[0] != 0:
        return 0
    
    for k in range(1, n):
        cnt = k-(sorted_cards[k]-1)
        if cnt <= 0:
            res = 0
            break
        res = (res * cnt) % MOD
    return res

c = [0,0,2]
res = ways_to_pick_cards(c)
print(res)
