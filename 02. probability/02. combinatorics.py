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
(2, 4)
(2, 6)
(2, 1)
(4, 6)
(4, 1)
(6, 1)
(2, 4, 6)
(2, 4, 1)
(2, 6, 1)
(4, 6, 1)
(2, 4, 6, 1)
"""
import math

def combinations(n, k):
    """
    C(n,k)=n!/k!(n-k)!
    """
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def solve_set_game(N, A):
    MOD = 10**9 + 7
    even_count = 0
    odd_count = 0
    
    for num in A:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    even_sum_subsets = 0
    if even_count > 0:
        for k in range(0, even_count + 1):
            even_sum_subsets += combinations(even_count, k)
        even_sum_subsets = even_sum_subsets - 1
    
    odd_even_sum_subsets = 0
    if odd_count > 0:
        for k in range(0, odd_count + 1, 2):
            odd_even_sum_subsets += combinations(odd_count, k)
    
    total_even_sum_subsets = even_sum_subsets * odd_even_sum_subsets % MOD
    return total_even_sum_subsets

N = 4
A = [2, 4, 6, 1]
print(solve_set_game(N, A))