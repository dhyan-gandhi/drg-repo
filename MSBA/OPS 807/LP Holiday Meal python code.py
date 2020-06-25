# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 00:17:08 2019

@author: jg
"""

"""
problem statement:
    
The Holiday Meal Turkey Ranch is considering buying two different brands of 
turkey feed and blending them to provide a good, low-cost diet for its turkeys 
    
X1 =   number of pounds of brand 1 feed purchased
X2 =   number of pounds of brand 2 feed purchased

Minimize cost (in cents) = 2X1 + 3X2		
subject to:
	5X1	+ 10X2	≥  90 ounces	(ingredient A constraint)
	4X1	+ 3X2	≥  48 ounces	(ingredient B constraint)
	0.5X1		≥ 1.5 ounces	(ingredient C constraint)
	    X1		≥  0			(nonnegativity constraint)
		    X2	≥  0			(nonnegativity constraint)


"""
"""
Solution using scipy.optimize.linprog
"""

import numpy as np
from scipy.optimize import linprog



A = np.array([[-5, -10], [-4, -3], [-0.5, 0]])
b = np.array([-90, -48, -1.5])
c = np.array([2, 3])

res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
print(f'Optimal value: {res.fun}, \nX: {res.x}')

"""
Solution using pulp library

"""

from pulp import *



"""
Solving using pulp library with integer programming capability

"""
model = LpProblem("Profit minimising problem", LpMinimize)

x1 = LpVariable('x1', lowBound=0, cat='Continuous')
x2 = LpVariable('x2', lowBound=0, cat='Continuous')

# Objective function
model += 2 * x1 + 3 * x2, "Cost"

# Constraints
model += 5 * x1 + 10 * x2 >= 90
model += 4 * x1 + 3  * x2 >= 48
model += 0.5 * x1 + 0.0* x2 >= 1.5

# Solve our problem
model.solve()
LpStatus[model.status]
#pulp.LpStatus[model.status]

"""
answer from excel solver:
    feed1 = 8.4
    feed2 = 4.8
    minimum cost = 31.2
"""

print(f'feed1 weight: {x1.varValue} \nfeed2 weight: {x2.varValue}')
print(f'Minimum cost is = {value(model.objective)}')

