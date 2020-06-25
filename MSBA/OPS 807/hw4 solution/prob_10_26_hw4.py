# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 02:27:56 2019

@author: jg
"""

"""
Problem 10.26 Hw4

S = dollars invested in stocks; 
B = dollars invested in bonds;
R = dollars invested in real estate

Minimize d1– + d2– + d3+

Subject to
0.13S + 0.08B + 0.10R +	Return is at least 10% (.10 * 250K)
d1– – d1+ = 25,000	
B + d2– – d2+ = 75,000	Amount in bonds is at least 30%
R + d3– – d3+ = 0.50(S + B)	Real estate should not exceed half of stocks and bonds
S + B + R = 250,000
S <= 150,000
B <= 150,000
R <= 150,000
S, B, R >= 0

b. 

S = $50,000 invested in stocks,
B = 75,000 invested in bonds;
R = $125,000 invested in real estate.

"""

import pulp


model = pulp.LpProblem("under/overachievement minimizing problem", pulp.LpMinimize)

S = pulp.LpVariable("S", lowBound=0, cat='Integer')
B = pulp.LpVariable("B", lowBound=0, cat='Integer')
R = pulp.LpVariable("R", lowBound=0, cat='Integer')
d1_neg = pulp.LpVariable("d1_neg", lowBound=0, cat='Integer')
d1_plus = pulp.LpVariable("d1_plus", lowBound=0, cat='Integer')
d2_neg = pulp.LpVariable("d2_neg", lowBound=0, cat='Integer')
d2_plus = pulp.LpVariable("d2_plus", lowBound=0, cat='Integer')
d3_neg = pulp.LpVariable("d3_neg", lowBound=0, cat='Integer')
d3_plus = pulp.LpVariable("d3_plus", lowBound=0, cat='Integer')




# Objective function
model += d1_neg + d2_neg + d3_plus, "under_over"
#model += d1_neg + d1_plus + d2_plus + d3_neg, "under_over"


# Constraints     
model += .13 * S + 0.08 * B + 0.1 * R + d1_neg - d1_plus == 25000.0  #(10% overall return goal)
model += B + d2_neg- d2_plus                   == 75000   # (Amount in bonds is at least 30%)
model += R + d3_neg - d3_plus                  == 0.5*(S + B)   #(Real estate should not exceed half of stocks and bonds)
model += S + B + R                             == 250000   # (three-drawer sales limit)
model += S <= 150000
model += B <= 150000
model += R <= 150000



# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( f"dollar invested in Stocks = {S.varValue}")
print( f"dollar invested in Bonds = {B.varValue}") 
print( f"dollar invested in RealEstate  = {R.varValue}") 
print( f"underachievement of Stock goal = {d1_neg.varValue}")
print( f"overachievement of Stock goal  = {d1_plus.varValue}") 
print( f"undererachievement of Bond goal  = {d2_neg.varValue:.0f}")
print( f"overrachievement of Bond goal = {d2_plus.varValue:.0f}") 
print( f"underachievement of RealEstate Investment goal = {d3_neg.varValue:.0f}") 
print( f"overachievement of RealEstate Investment goal = {d3_plus.varValue:.0f}") 