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
def calculate_probability(A, B, C):
    area_rectangle = A * B
    
    if C <= 0:
        return 0
    elif C >= A + B:
        return 1
    else:
        if C <= A and C <= B:
            area_triangle = 0.5 * C * C
        elif C > A and C > B:
            triangle_out = 0.5 * (C - A) * (C - B)
            area_triangle = 0.5 * C * C - triangle_out
        elif C > A:
            triangle_out = 0.5 * (C - A) * (C - A)
            area_triangle = 0.5 * C * C - triangle_out
        elif C > B:
            triangle_out = 0.5 * (C - B) * (C - B)
            area_triangle = 0.5 * C * C - triangle_out
        return area_triangle / area_rectangle

inputs = [(1, 1, 1), (1, 1, 2), (1, 1, 3)]
results = [calculate_probability(A, B, C) for A, B, C in inputs]
print(results)
