# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:19:58 2018

@author: jahan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""" Remember that scipy.optimize always minimizes so
to convert a maximization problem into minimization replace
f(x) by -f(x)


"""
""" problem statement
Flair Furniture produces inexpensive tables and chairs
Processes are similar, both require carpentry work and painting and varnishing
Each table takes 4 hours of carpentry and 2 hours of painting and varnishing
Each chair requires 3 of carpentry and 1 hour of painting and varnishing
There are 240 hours of carpentry time available and 100 hours of painting and varnishing
Each table yields a profit of $70 and each chair a profit of $50


1. Write the problem above using LP and give a solution


Maximize profit for the flair furniture company
maximize f(x)=70T + 50C
4T + 3C ≤ 240
2T + 1C ≤ 100
T, C ≥ 0
"""

import numpy as np
from scipy.optimize import linprog


"""
solving the problem using scipy.optimize.linprog

"""

A = np.array([[4, 3], [2,1]])
b = np.array([240, 100])
c = np.array([-70, -50])

"""
answer from excel solver:
    Tables = 30
    chairs = 40
    total profit = $4100.0
"""

res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
print(f'Optimal value: {-res.fun}, \nX: {res.x}')

"""
Created on Fri 7/26/2019 

pulp library implementation of Flair furniture

@author: jahan
"""




#import pulp 
from pulp import *



"""
Solving using pulp library with integer programming capability

"""
model = LpProblem("Profit maximising problem", LpMaximize)


x1 = LpVariable('x1', lowBound=0, cat='Continuous')
x2 = LpVariable('x2', lowBound=0, cat='Continuous')

# Objective function
model += 70 * x1 + 50 * x2, "Profit"

# Constraints
model += 4 * x1 + 3 * x2 <= 240
model += 2 * x1 + x2     <= 100

# Solve our problem
model.solve()
LpStatus[model.status]

"""
answer from excel solver:
    Tables = 30
    chairs = 40
    total profit = $4100.0
"""
 

print(f' Number of tables: {x1.varValue} \nNumber of chairs: {x2.varValue}')
print(f'Total profit is = {value(model.objective)}')

