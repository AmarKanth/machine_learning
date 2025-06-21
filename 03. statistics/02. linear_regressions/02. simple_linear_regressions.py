"""
Simple linear regression

y = β₀ + β₁X₁ + ε

y : y is the variable we are trying to predict and is called dependent variable.
β₀(beta zero) : intercept(bias)
β₁(beta one) : coeffiecient(slope)
X₁ : input feature, it is independent variable
ε(epsilon) = error term

when we using the regression analysis, we want to predict the value of y provided we have 
the value of x.

but to have regression y is dependent on x in some causal way. whenever there is a 
change in x, such change must translate into a change in y.
"""

"""
Example :
1. The income a person receives depends on the number of years of education that person 
has received.
2. Here the dependent variable is income, while the independent variable is years of 
education.
3. There is causal relation between two, the more education you get, the higher income 
you are likely to receive.
4. Reverse relation is education depends on income. The higher your income, the more years
you spend educating yourself. The causal relationship is not correct.
5. In our model there are coefficients, β₁ is coefficient it is before the independent 
variable. It quantifies the effect of education on income. If β₁=50, then for each 
additional year of education, your income would grow by $50
6. In this example think about β₀ is the minimum wage.
7. ε is error of estimation, the error is the actual difference between the observed 
income and the income regression predicted. on average accross all the observations, 
the error is zero. If you earn more than what the regression is predected, then 
someone earns less than what the regression predected everything evens out. 
"""

"""
ŷ = b₀ + b₁x₁

ŷ(y hat) : whenever we have hat it is an estimated or predicted value.
b₀ : is the estimated of the regression constant β₀
b₁ : is the estimated of β₁ and x
x₁ : is the sample data for the independent variable
"""

"""
You have an ice-cream shop. You noticed a relationship between the number of cones 
you order and the number of ice-creams you sell. Is this a suitable situation for 
regression analysis?

If you run out of cones, you cant sell anymore ice creams, this is not 
regression analysis material. The two variables go hand in hand as (ususally) 
each ice cream requires cone.
"""

"""
You are trying to predict the amount of beer consumed in the US, 
depending on the state. Is this regression material?

Beer_Consumption = β₀ + β₁*Population + β₂*Avg_Temperature + β₃*Brewery_Count + ε
"""