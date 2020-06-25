# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 00:33:34 2019

@author: jg
"""
"""
Student Enterprises sells two sizes of wall posters, a large 3- by 4-foot poster 
and a smaller 2- by 3-foot poster. The profit earned from the sale of each 
large poster is $3; each smaller poster earns $2. The firm, although profitable, 
is not large; it consists of one art student, Jan Meising, at the University 
of Kentucky. Because of her classroom schedule, Jan has the following weekly 
constraints: 
    (1) up to three large posters can be sold, 
    (2) up to five smaller posters can be sold, 
    (3) up to 10 hours can be spent on posters during the week, with each 
        large poster requiring 2 hours of work and each small one taking 1 hour. 
 With the semester almost over, Jan plans on taking a three-month summer vacation
to England and doesn’t want to leave any unfinished posters behind. 
Find a solution that maximizes the profit using the following methods:
    1.	Graphical approach for the maximum profit (LP method).
    2.	Find an integer solution for the maximum profit.
    3.	Solve the problem with the help of a computer.
    4.	Explain the difference between the integer solution and truncating the LP solution if different.

"""

"""
Solution using pulp
"""

from pulp import *



model = LpProblem("Profit Maximization problem", LpMaximize)

# Pure LP solution
#x1 = LpVariable('x1', lowBound=0, cat='Continuous')
#x2 = LpVariable('x2', lowBound=0, cat='Continuous')

# integer solution
x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')


# Objective function
model += 3*x1+2*x2, "Profit"

# Constraints
model += x1 <= 3
model += x2 <= 5
model += 2*x1 + x2 <= 10

# Solve our problem
model.solve()
LpStatus[model.status]

 

print(f'Number of large posters: {x1.varValue},  \nNumber of small posters: {x2.varValue}')
print(f'Total Profit is = ${value(model.objective)}')
