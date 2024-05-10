"""
Probability of an Event – If there are total p possible outcomes associated with a random experiment 
and q of them are favourable outcomes to the event A, then the probability of event A is 
denoted by P(A) and is given by

P(A) = q/p
The probability of non-occurrence of event A, i.e, P(A’) = 1 – P(A)

Note –
If the value of P(A) = 1, then event A is called a sure event.
If the value of P(A) = 0, then event A is called an impossible event.
Also, P(A) + P(A’) = 1
"""

"""
Theorems:
General – Let A, B, and C are the events associated with a random experiment, then
P(A∪B) = P(A) + P(B) – P(A∩B)
P(A∪B) = P(A) + P(B) if A and B are mutually exclusive
P(A∪B∪C) = P(A) + P(B) + P(C) – P(A∩B) – P(B∩C)- P(C∩A) + P(A∩B∩C)
P(A∩B’) = P(A) – P(A∩B)
P(A’∩B) = P(B) – P(A∩B)

Extension of Multiplication Theorem – Let A1, A2, ….., An are n events associated with a random experiment, 
then P(A1∩A2∩A3 ….. An) = P(A1)P(A2/A1)P(A3/A2∩A1) ….. P(An/A1∩A2∩A3∩ ….. ∩An-1)
"""

"""
Experimental Probabilities
P(A) = successful-trails/all-trails

Expected outcome = Theoritical outcome * number of trails
E(A) = P(A) * n
"""

"""
(1) A bag contains 10 oranges and 20 apples out of which 5 apples and 3 oranges are defective. 
If a person takes out two at random, what is the probability that either both are 
good or both are apples? 
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
