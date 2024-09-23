"""
P(A|B) : Means event (A) happening given that another event (B) has already occurred. In probability notation 
this is denoted as A given B.

Conditional Probability Formula when events are dependent
P(A|B) = P (A ∩ B) / P(B)

Conditional Probability Formula when events are independent
P(A|B) = P (A)
"""

"""
Properties of Conditional Probability 

Property 1: Let’s consider an event A in any sample space S of an experiment.
            P(S|A) = P(A|A) = 1

Property 2: For any two events A and B of a sample space S, and an event X such that P(X) ≠ 0,
            P((A ∪ B)|X) = P(A|X) + P(B|X) – P((A ∩ B)|X)

Property 3: The order of set or events is important in conditional probability, i.e.
            P(A|B) ≠ P(B|A)

Property 4: The complement formula for probability only holds conditional probability if it is given 
in the context of the first argument in conditional probability i.e.
            P(A’|B)=1-P(A|B)
            P(A|B’) ≠ 1-P(A|B)

Property 5: For any two or three independent events, the intersection of events can be calculated 
using the following formula:
    For the intersection of two events A and B,
    P(A ⋂ B) = P(A) P(B)

    For the intersection of three events A, B, and C,
    P (A ⋂ B ⋂ C) = P(A) P(B) P(C)
"""

"""
Multiplication Rule of Probability
P(A∩B) = P(A) × P(B∣A)
"""

"""
A bag contains 5 red balls and 7 blue balls. Two balls are drawn without 
replacement. What is the probability that the second ball drawn is red, given 
that the first ball drawn was red?
"""
initial_red_balls = 5
initial_blue_balls = 7
total_balls = initial_red_balls + initial_blue_balls
p_A = initial_red_balls / total_balls
remaining_red_balls = initial_red_balls - 1
remaining_total_balls = total_balls - 1
p_B_given_A = remaining_red_balls / remaining_total_balls
print(p_B_given_A)

"""
A box contains 5 green balls and 3 yellow balls. Two balls are drawn without replacement. 
What is the probability that both balls are green?
"""
from fractions import Fraction

P_A = Fraction(5, 8)
P_B_given_A = Fraction(4, 7)
P_A_and_B = P_A * P_B_given_A
print(P_A_and_B)

"""
In a bag, there are 8 red marbles, 4 blue marbles, and 3 green marbles. 
If one marble is randomly drawn, what is the probability that it is not blue?
"""
from fractions import Fraction

total_marbles = 8 + 4 + 3
blue_marbles = 4
p_blue = Fraction(blue_marbles, total_marbles)
p_not_blue = 1 - p_blue
print(p_not_blue)

"""
In a survey among a group of students, 70% play football, 60% play basketball, 
and 40% play both sports. If a student is chosen at random and it is 
known that the student plays basketball, what is the probability that 
the student also plays football?
"""
from fractions import Fraction

total_students = 100
students_play_football = 70
students_play_basketball = 60
students_play_both = 40

p_football_given_basketball = Fraction(students_play_both, students_play_basketball)
print(p_football_given_basketball)


"""
In a deck of 52 playing cards, 4 cards are drawn without replacement. What is the 
probability that all 4 cards are aces, given that the first card drawn is an ace?
"""
from fractions import Fraction

P_A = Fraction(4, 52)
P_B_given_A = Fraction(3, 51)
P_C_given_A_and_B = Fraction(2, 50)
P_D_given_A_and_B_and_C = Fraction(1, 49)

P = P_A * P_B_given_A * P_C_given_A_and_B * P_D_given_A_and_B_and_C
print(P)
