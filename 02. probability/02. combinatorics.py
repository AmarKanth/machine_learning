"""
Welcome to the exciting class of Professor Manasa. In each lecture she used to play 
some game while teaching a new concept. Today's topic is Set Theory. For today's game, 
she had given a set A = {a1, a2, ...aN} of N integers to her students and asked them 
to play the game as follows.

At each step of the game she calls a random student and asks him/her to select a 
non-empty subset from set A such that this subset had not been selected earlier 
and the sum of subset should be even. This game ends when all possible subsets had 
been selected. Manasa needs your help in counting the total number of times students 
can be called assuming each student gives the right answer. While it is given that 
if two numbers are same in the given set, they have different colors. 
It means that if a1 = a2, then choosing a1 and choosing a2 will be considered as different 
sets.
"""
from itertools import combinations

def count_even_sum_subsets(elements):
    MOD = 10**9 + 7
    even_sum_count = 0

    for r in range(1, len(elements) + 1):
        for combo in combinations(elements, r):
            if sum(combo) % 2 == 0:
                even_sum_count += 1

    return even_sum_count % MOD

N = 4
A = [2, 4, 6, 1]
result = count_even_sum_subsets(A)
print(result)


"""
There are N cards on the table and each has a number between 0 and N. 
Let us denote the number on the ith card by ci. 
You want to pick up all the cards. The ith card can be picked up only if 
at least ci cards have been picked up before it. (As an example, if a card has a 
value of 3 on it, you can't pick that card up unless you've already picked up 
3 cards previously) In how many ways can all the cards be picked up?
"""
def ways_to_pick_cards(n, cards):
    sorted_cards = sorted(cards)
    res = 1
    if sorted_cards[0] != 0:
        return 0
    
    for k in range(1, n):
        cnt = k-(sorted_cards[k]-1)
        if cnt <= 0:
            res = 0
            break
        res = (res * cnt)
    return res

c = [0,0,2]
res = ways_to_pick_cards(len(c), c)
print(res)