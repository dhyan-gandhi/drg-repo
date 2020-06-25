# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:22:58 2019

Assignment problem, optimal work distribution

@author: jg
"""

"""
The Fix-it Shop has just received three new repair projects that must be repaired quickly
1.A radio
2.A toaster oven
3.A coffee table

Three workers with different talents are able to do the jobs
Owner estimates wage cost for workers on projects
Objective –minimize total cost

Let
Xij = 1 if person i is assigned to task j, 0 otherwise

where
i=1, 2, 3, with 1 = Adams, 2 = Brown, and 3 = Cooper
j=1, 2, 3, with 1 = Project 1, 2 = Project 2, and 3 = Project 3

Minimize total cost = 11X11 + 14X12 + 6X13 + 8X21
+ 10X22 + 11X23 + 9X31
+ 12X32 + 7X33

subject to
X11 + X12 + X13 = 1
X21 + X22 + X23 = 1
X31 + X32 + X33 = 1
X11 + X21 + X31 = 1
X12 + X22 + X32 = 1
X13 + X23 + X33 = 1
Xij = 0 or 1 for all i and j

"""

import pulp  


"""
Solving using pulp library for integer/binary programming 

"""
model = pulp.LpProblem("Assignment problem", pulp.LpMinimize)

X11 = pulp.LpVariable("X11", lowBound=0, cat='Binary')
X12 = pulp.LpVariable("X12", lowBound=0, cat='Binary')
X13 = pulp.LpVariable("X13", lowBound=0, cat='Binary')
X21 = pulp.LpVariable("X21", lowBound=0, cat='Binary')
X22 = pulp.LpVariable("X22", lowBound=0, cat='Binary')
X23 = pulp.LpVariable("X23", lowBound=0, cat='Binary')
X31 = pulp.LpVariable("X31", lowBound=0, cat='Binary')
X32 = pulp.LpVariable("X32", lowBound=0, cat='Binary')
X33 = pulp.LpVariable("X33", lowBound=0, cat='Binary')



# Objetive function
model += 11*X11 + 14*X12 + 6*X13 + 8*X21 + 10*X22 + 11*X23 + 9*X31+ 12*X32 + 7*X33
#model += 18*x1 + 15*x2 + 14*x3, "NPV Maximization"

# constraints
model += X11 + X12 + X13 == 1
model += X21 + X22 + X23 == 1
model += X31 + X32 + X33 == 1
model += X11 + X21 + X31 == 1
model += X12 + X22 + X32 == 1
model += X13 + X23 + X33 == 1


# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print(f'Adam assigned to project 1 = {X11.varValue:.0f}')
print(f'Adam assigned to project 2 = {X12.varValue:.0f}')
print(f'Adam assigned to project 3 = {X13.varValue:.0f}') 
print(f'Brown assigned to project 1 = {X21.varValue:.0f}')
print(f'Brown assigned to project 2 = {X22.varValue:.0f}')
print(f'Brown assigned to project 3 = {X23.varValue:.0f}')
print(f'Cooper assigned to project 1 = {X31.varValue:.0f}')
print(f'Cooper assigned to project 2 = {X32.varValue:.0f}')
print(f'Cooper assigned to project 3 = {X33.varValue:.0f}')
print(f'Total Cost is = ${pulp.value(model.objective)}')


