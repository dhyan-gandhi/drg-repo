# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 2019

@author: jg
"""

"""
In this problem since the decision is based on presence of one or two or all the projects, we
need to resort to binary decision variables. Our objective is to maximize NPV:

Let X1 = 1 if apartment project is undertaken; 0 otherwise
Let X2 = 1 if shopping center project is undertaken; 0 otherwise
Let X3 = 1 if mini-warehouse project is undertaken; 0 otherwise

Maximize NPV = 18X1 + 15X2 + 14X3

Subject to:
    
40X1 + 30X2 + 20X3 <= 80
30X1 + 20X2 + 20X3 <= 50
X1, X2, X3 = 1 or 0

"""

from pulp import *


"""
Solving using pulp library for integer/binary programming 

"""
model = LpProblem("Real Estate NPV maximization problem", LpMaximize)

x1 = LpVariable("x1", lowBound=0, cat='Binary')
x2 = LpVariable("x2", lowBound=0, cat='Binary')
x3 = LpVariable("x3", lowBound=0, cat='Binary')

# Objetive function

model += 18*x1 + 15*x2 + 14*x3, "NPV Maximization"

# constraints
model += 40 * x1 + 30 * x2 + 20 * x3 <= 80
model += 30 * x1 + 20 * x2 + 20 * x3 <= 50


# Solve our problem
model.solve()
LpStatus[model.status]


# Print our decision variable values
print(f'Apartment Project = {x1.varValue:.0f}')
print(f'Shopping center project = {x2.varValue:.0f}') 
print(f'Mini-warehouse project = {x3.varValue:.0f}') 
print(f'Maximum NPV  = ${value(model.objective)*1000:.2f}')


