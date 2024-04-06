"""
A 		=> Event
P(A) 	=> Probability

P(A) = preferred-outcomes/all-outcomes
"""

"""
Experimental Probabilities
P(A) = successful-trails/all-trails

Expected outcome = Theoritical outcome * number of trails
E(A) = P(A) * n
"""

"""
Given two numbers A and B and we generate x and y using the random number generator with 
uniform probability density function [0, A] and [0, B] respectively, 
what's the probability that x + y is less than C?

Input
3
1 1 1
1 1 2
1 1 3
"""
def calculate_probability(a, b, c):
    if c <= a + b:
        if c <= min(a,b):
            return (c*c)*1/(2*a*b)
        else:
            return c*(c-min(a,b)) * min(a,b)/(2*a*b)
    return 1

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        res = calculate_probability(a, b, c)
        print(res)