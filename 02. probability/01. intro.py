"""
(1) Probability of an Event – If there are total p possible outcomes associated with a random experiment 
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
(2) Theorems:
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
(3) Probability Density Function
The Probability Density Function (PDF) is the probability function that is the density of a 
continuous random variable that lies between a range of certain values. Probability density 
function explains how the normal distribution and how mean and deviation exist in the system.
"""


"""
(4) A bag contains 10 oranges and 20 apples out of which 5 apples and 3 oranges are defective. 
If a person takes out two at random, what is the probability that either both are 
good or both are apples?
The combination formula is:
n!/k!(n-k)!
"""
import math

ways_to_select_two_fruits = math.comb(30,2)
ways_to_select_two_apples = math.comb(20,2)

ways_to_select_two_good_fruits = math.comb(22,2)
ways_to_select_two_good_apples = math.comb(15,2)

P_A = ways_to_select_two_apples / ways_to_select_two_fruits
P_B = ways_to_select_two_good_fruits / ways_to_select_two_fruits
P_A_INTERSECT_B = ways_to_select_two_good_apples / ways_to_select_two_fruits
P_A_UNION_B = P_A + P_B - P_A_INTERSECT_B
print(P_A_UNION_B)


"""
(5) The probability that a person will get an electric contract is 2/5 and 
the probability that he will not get a plumbing contract is 4/7. 
If the probability of getting at least one contact is 2/3, what is the 
probability of getting both? 
"""
from fractions import Fraction

person_gets_electric_contract = Fraction(2,5)
person_does_not_get_plumbing_contract = Fraction(4,7)
has_at_least_one_contract = Fraction(2,3)

P_A = person_gets_electric_contract
P_B = 1 - person_does_not_get_plumbing_contract
P_A_UNION_B = has_at_least_one_contract

P_A_INTERSECT_B = P_A + P_B - P_A_UNION_B
print(float(P_A_INTERSECT_B))


"""
(6) Find the probability of getting a multiple of 3 when a die is rolled.
"""
total_outcomes = 6
multiples_of_3 = [i for i in range(1,total_outcomes+1) if i%3==0]
num_favorable_outcomes = len(multiples_of_3)
probability = num_favorable_outcomes / total_outcomes
print(probability)


"""
(7) Total Law of Probability – Let S be the sample space associated with a random 
experiment and E1, E2, …, En be n mutually exclusive and exhaustive events associated 
with the random experiment. If A is any event that occurs with E1 or E2 or … or En, then
P(A) = P(E1)P(A/E1) + P(E2)P(A/E2) + ... +  P(En)P(A/En)
"""


"""
(8) A bag contains 3 black balls and 4 red balls. A second bag contains 4 black balls 
and 2 red balls. One bag is selected at random. From the selected bag, one ball is drawn. 
Find the probability that the ball drawn is red.
"""
from fractions import Fraction

P_Selecting_FirstBag = Fraction(1,2)
P_Selecting_SecondBag = Fraction(1,2)
P_Red_FirstBag = Fraction(4,7)
P_Red_SecondBag = Fraction(2,6)

P_A = P_Selecting_FirstBag*P_Red_FirstBag + P_Selecting_SecondBag*P_Red_SecondBag
print(P_A)


"""
(9) In a bulb factory, three machines namely A, B, C produces 25%, 35% and 40% of the 
total bulbs respectively. Of their output, 5, 4 and 2 percent are defective bulbs 
respectively. A bulb is drawn at random from products. What is the probability 
that bulb drawn is defective?
"""
from fractions import Fraction

bulb_from_MachineA = Fraction(25, 100)
bulb_from_MachineB = Fraction(35, 100)
bulb_from_MachineC = Fraction(40, 100)

defective_bulb_from_MachineA = Fraction(5, 100)
defective_bulb_from_MachineB = Fraction(4, 100)
defective_bulb_from_MachineC = Fraction(2, 100)

p1 = bulb_from_MachineA*defective_bulb_from_MachineA
p2 = bulb_from_MachineB*defective_bulb_from_MachineB
p3 = bulb_from_MachineC*defective_bulb_from_MachineC

p = p1 + p2 + p3
print(float(p))


"""
(10) Find the probability of getting a card of kings from a deck of 52 cards.
"""
total_outcomes = 52
num_favorable_outcomes = 4
probability = num_favorable_outcomes / total_outcomes
print(probability)


"""
(11) Find the probability of picking vowels in the word 'CHAMPION'
"""
word = "CHAMPION"
vowels = 'AEIOU'
total_letters = len(word)
vowel_count = sum(1 for letter in word if letter in vowels)
probability = vowel_count / total_letters
print(probability)


"""
(12) A bag is filled with balls. Some of these balls are red in color. The probability 
of picking a red ball is x/2. Find the value of x if the probability of picking 
a non-red ball is 2/3.
"""
P_non_red = 2 / 3
P_red = 1 - P_non_red
x = 2 * P_red
print(x)


"""
(13) There are 24 students in a class. Out of these, 24 students, 16 are boys and the 
remaining are girls. Find the probability of selecting a girl randomly.
"""
total_students = 24
boys = 16
girls = total_students - boys
probability_girl = girls / total_students
print(probability_girl)


"""
(14) There are 20 defective bulbs in a box of 500 electric bubs. Find the probability 
of randomly selecting a non-defective bulb.
"""
total_bulbs = 500
defective_bulbs = 20
non_defective_bulbs = total_bulbs - defective_bulbs
probability_non_defective = non_defective_bulbs / total_bulbs
print(probability_non_defective)


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
