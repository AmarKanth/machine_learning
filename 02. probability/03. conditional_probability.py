"""
P(A|B) : Means event (A) happening given that another event (B) has already occurred. In probability notation 
this is denoted as A given B.
"""

"""
Conditional Probability Formula when events are dependent
P(A|B) = P (A ∩ B) / P(B)
"""

"""
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

