# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 01:32:53 2019

@author: jg
"""

"""


a.    
Maximize profit =	$5,000X1 + 6,000X2 + 10,000X3
	+ 12,000X4 + 8,000X5 + 3,000X6
	+ 9,000X7 + 10,000X8
subject to	$60,000X1 + 50,000X2 + 82,000X3
	+ 103,000X4 + 50,000X5
	+ 41,000X6 + 80,000X7
	+ 69,000X8  $300,000
    
Solution:    
b.  X1 = 0, X2 = 1, X3 = 1, X4 = 0, X5 = 1, X6 = 1, X7 = 0, X8 = 1, Profit = $37,000
 

"""

from pulp import *



model = LpProblem("Profit Maximization problem", LpMaximize)

#constUpBnd = 20000

x1 = LpVariable('x1', lowBound=0, cat='Binary')
x2 = LpVariable('x2', lowBound=0,  cat='Binary')
x3 = LpVariable('x3', lowBound=0,  cat='Binary')
x4 = LpVariable('x4', lowBound=0,  cat='Binary')
x5 = LpVariable('x5', lowBound=0, cat='Binary')
x6 = LpVariable('x6', lowBound=0,  cat='Binary')
x7 = LpVariable('x7', lowBound=0, cat='Binary')
x8 = LpVariable('x8', lowBound=0,  cat='Binary')



# Objective function
model += 5000.0*x1 + 6000.0*x2 + 10000.0*x3 + 12000.0*x4 + 8000.0*x5 + 3000.0*x6 + 9000.0*x7 + 10000.0*x8, "Profit" 

# Constraints
model += 60000.0*x1 + 50000.0*x2 + 82000.0*x3 + 103000.0*x4 + 50000.0*x5 + 41000.0*x6 + 80000 * x7 + 69000.* x8 <= 300000.0


# Solve our problem
model.solve()
LpStatus[model.status]

"""
Optimal solution will result in 3. Only 3 locations are needed
x1=x3=x4=0, the rest are 1

"""
 

print(f'x1: {x1.varValue:.0f}, x2: {x2.varValue:.0f}, x3: {x3.varValue:.0f}, x4: {x4.varValue:.0f}, x5: {x5.varValue:.0f}, x6: {x6.varValue:.0f},  x7: {x7.varValue:.0f},  x8: {x8.varValue:.0f}')
print(f'Expected Profit = {value(model.objective):.0f}')
