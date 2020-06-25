# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:31:35 2019

@author: jg
"""

"""
Problem 10.18

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

other requirements/constraints:

    (a) Suppose that the shopping center and the apartment
would be on adjacent properties, and the
shopping center would only be considered if the
apartment were also built. Formulate the constraint
that would stipulate this.

This requirement results in this extra constraint  x1 >= x2 x1 - x2 >= 0 which
means if x1 is a no go then x2 will be a no go as well, i.e. if x1 == 0 then x2 = 0

(b) Formulate a constraint that would force exactly
two of the three projects to be undertaken.

This constraint for binary variables is x1 + x2 + x3 = 2


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
# case a when shopping mall depends on residential project
model += x1 - x2 >= 0
# case b when only 2 out of 3 project will be undertaken
model += x1 + x2 + x3 == 2 

# Solve our problem
model.solve()
LpStatus[model.status]


# Print our decision variable values
print(f'Apartment Project = {x1.varValue:.0f}')
print(f'Shopping center project = {x2.varValue:.0f}') 
print(f'Mini-warehouse project = {x3.varValue:.0f}') 
print(f'Maximum NPV  = ${value(model.objective)*1000:.2f}')


