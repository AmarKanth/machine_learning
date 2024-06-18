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

