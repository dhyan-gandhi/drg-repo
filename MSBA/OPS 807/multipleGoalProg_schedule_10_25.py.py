# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 2019

@author: jg
"""

"""
Problem 10.25 Goal programming

Decision variables:
    
X1 = number of hours of sleep needed per week
X2 = number of personal hours eating, personal hygiene, handling laundary, and so on
X3 = number of hours of class and studying
X4 = number of hours of social time off base dating, sports, family visits, and so on    
    
    d1–	 = underachievement of class and study goal
	d1+	= overachievement of class and study goal
	d2+	= overachievement of sleeping goal
	d3–	= underachievement of social time goal
Major Bligh’s objective function becomes
minimize = d1– + d1+ + d2+ + d3–

subject to constraints (per week)
	1X1 + 1X2 + 1X3 + 1X4	== 168
	1X3 + d1–    – d1+	== 30
	1X1 –    d2+	== 49
	1X4 + d3–	== 20
All variables >= 0

Since the goals have priority, they can be rewritten in this order, yielding to the absolute com-pletion of each goal before attempting to achieve the next goal. The objective function would become
Minimize = P1d1– + P1d1+ + P2d2+ + P3d3–
where	P1 = meet class and study goal
	P2 = meet sleeping goal
	P3 = meet socializing goal


"""

import pulp



"""
Solving using pulp library for goal programming 

"""
model = pulp.LpProblem("under/overachievement minimizing problem", pulp.LpMinimize)

x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')
x3 = pulp.LpVariable("x3", lowBound=0, cat='Integer')
x4 = pulp.LpVariable("x4", lowBound=0, cat='Integer')
d1_neg = pulp.LpVariable("d1_neg", lowBound=0, cat='Integer')
d1_plus = pulp.LpVariable("d1_plus", lowBound=0, cat='Integer')
d2_plus = pulp.LpVariable("d2_plus", lowBound=0, cat='Integer')
d3_neg = pulp.LpVariable("d3_neg", lowBound=0, cat='Integer')


# Priorities are the same but no weights
# objective function = P1d1– + P2d2– + P3d3+ + P4(2d4–) + P4d5–
p1 = 1
p2 = 2
p3 = 3




# Objective function
model += p1 * d1_neg + p1 * d1_plus + p2 * d2_plus + p3 * d3_neg, "under_over"
#model += d1_neg + d1_plus + d2_plus + d3_neg, "under_over"

# Constraints
# pay attention to the first constraint. if you make it <= you will get x2 = 0
model += x1 + x2 + x3 + x4     == 168
model += x1 - d2_plus          == 49
model += x3 + d1_neg - d1_plus == 30
model += x4 + d3_neg           == 20




# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( "number of hours of sleep = {}".format(x1.varValue))
print( "number of personal hours eating, personal = {}".format(x2.varValue)) 
print( "number of hours of class and studying = {}".format(x3.varValue)) 
print( "number of hours of social time off = {}".format(x4.varValue)) 
print( "underachievement of class and study goal = {}".format(d1_neg.varValue))
print( "overachievement of class and study goal  = {}".format(d1_plus.varValue)) 
print( "overachievement of sleeping goal  = {}".format(d2_plus.varValue))
print( "underachievement of social time goal = {}".format(d3_neg.varValue)) 
