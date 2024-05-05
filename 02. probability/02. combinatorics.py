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