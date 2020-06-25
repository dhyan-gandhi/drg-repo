# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:09:41 2019

@author: jg
"""

"""
The company manufactures quality speakers and stereo receivers
Products require a certain amount of skilled artisanship which is in limited supply
Product mix LP model

Maximize profit = 50 X1 + 120 X2
subject to:
    
    2X1 + 4X2 <= 80 hrs of electricians' time
    3X1 + X2  <= 60 hrs of audio technicians' time
    X1,X2     >= 0
    
optimal solution from Excel
    X1 = 0 Speakers
    X2 = 20 Receivers
    Profits = $2,400


"""
import numpy as np
from scipy.optimize import linprog
 
A = np.array([[2, 4], [3, 1]])
b = np.array([80, 60])
c = np.array([-50, -120])

res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None))
print(f'Maximum profit : {-res.fun}, \nX: {res.x}')

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
model += 50 * x1 + 120 * x2, "Profit"

# Constraints
model += 2 * x1 + 4 * x2 <= 80
model += 3 * x1 + x2     <= 60

# Solve our problem
model.solve()
LpStatus[model.status]

"""
optimal solution from Excel
    X1 = 0 Speakers
    X2 = 20 Receivers
    Profits = $2,400
"""
 

print(f' Number of Speakers: {x1.varValue} \nNumber of Receivers: {x2.varValue}')
print(f'Total profit is = {value(model.objective)}')

