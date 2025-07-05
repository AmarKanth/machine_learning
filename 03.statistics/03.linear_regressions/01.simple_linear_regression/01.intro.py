"""
ŷ  : y hat
β₀ : beta zero
β₁ : beta one
ε  : epsilon
"""

"""
linear regression :
A linear regression is a linear approximation of a causal relationship between two or 
more variables.
regression models are one of the most common ways to make inference and predictions.
"""

"""
Simple linear regression

y = β₀ + β₁X₁ + ε

y  : It is the variable we are trying to predict and is called dependent variable.
β₀ : Intercept(bias)
β₁ : Coeffiecient(slope)
X₁ : Input feature, it is independent variable
ε  : Error term

when we using the regression analysis, we want to predict the value of y provided we have 
the value of x.

There should be causal relation between y and x. whenever there is a change in x, 
such change must translate into a change in y.
"""

"""
Example :
1. The income a person receives depends on the number of years of education that person 
has received.
2. Here the dependent variable is income, while the independent variable is years of 
education.
3. There is causal relation between two, the more education you get, the higher income 
you are likely to receive.
4. Reverse relation is education depends on income. Meaning the more money you have, the 
more years you spend in school. The causal relationship is not correct.
5. In our model, there are coefficients. β₁ is the coefficient in front of the 
independent variable, and it measures the effect of education on income. 
If β₁ = 50, it means that for each additional year of education, income increases 
by $50.
6. In this example think about β₀ is the minimum wage.
7. ε is error of estimation, the error is the actual difference between the real 
income and the income regression predicted. on average accross all the observations, 
the error is zero. If you earn more than what the regression is predected, then 
someone earns less than what the regression predected everything evens out. 
"""

"""
ŷ = b₀ + b₁x₁

ŷ  : whenever we have hat it is an estimated or predicted value.
b₀ : is the estimated of the regression constant β₀
b₁ : is the estimated of β₁ and x
x₁ : is the sample data for the independent variable
"""

"""
What is the difference between correlation and regression?

Correlation :
1. Represents the relationship between two variables
2. Shows that two variables move together (no matter in which direction)
3. Symmetrical w.r.t. the two variables: ρ(x,y)=ρ(y,x)
4. A single point (a number)

Rgression :
1. Represents the relationship between two or more variables
2. Shows cause and effect (one variable is affected by the other)
3. One way – there is always only one variable that is causally dependent
4. A line (in 2D space)
"""