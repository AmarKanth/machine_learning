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


"""
Isaac has to buy a new HackerPhone for his girlfriend Amy. 
He is exploring the shops in the town to compare the prices whereupon 
he finds a shop located on the first floor of a building, 
that has a unique pricing policy. There are N steps leading to the shop. 
A numbered ball is placed on each of the steps.

The shopkeeper gives Isaac a fair coin and asks him to toss the coin 
before climbing each step. If the result of the toss is a 'Heads', 
Isaac should pick up the ball, else leave it and proceed to the next step.

The shopkeeper then asks Isaac to find the sum of all the numbers he 
has picked up (let's say S). The price of the HackerPhone is then the 
expected value of S. Help Isaac find the price of the HackerPhone.

Concept:
Each ball on a step has a 50% chance of being picked up 
(when the coin toss results in 'Heads') and a 50% chance of not being picked up 
(when the coin toss results in 'Tails').

Given n steps, and each step i having a ball with number a(i), the expected value E 
for each ball being picked is simply 1/2*a(i) because there's a 
50% chance of picking it up.

Calculation of the Expected Value:
To find the expected value S of all numbers Isaac picks up:
E(S)=E(a1)+E(a2)+...+E(an)
E(ai)=1/2*ai
"""
expected_value = 0.0
numbers_on_the_ball = [1,1,2]
for number in numbers_on_the_ball:
    expected_value += 0.5 * number
print(expected_value)
