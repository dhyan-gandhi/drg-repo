# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 01:59:17 2019

@author: jg
"""

"""
Geraldine Shawhan is president of Shawhan File
Works, a firm that manufactures two types of metal
file cabinets. The demand for her two-drawer model
is up to 600 cabinets per week; demand for a three drawer
cabinet is limited to 400 per week. Shawhan
File Works has a weekly operating capacity of 1,300
hours, with the two-drawer cabinet taking 1 hour
to produce and the three-drawer cabinet requiring
2 hours. Each two-drawer model sold yields a
$10 profit, and the profit for the large model is $15.
Shawhan has listed the following Shawhan has listed the following as a plan 
it wishes to achieve in order of importance:

    1. Attain a profit as close to $11,000 as possible
    each week.
    2. Avoid underutilization of the firm’s production
    capacity.
    3. Sell as many two- and three-drawer cabinets
    as the demand indicates.

Decision variables:
    
.   X1	= number of two-drawer cabinets produced each week
	X2	= number of three-drawer cabinets produced each week
	d1–	= underachievement of profit goal
	d1+	= overachievement of profit goal
	d2–	= idle time in production capacity
	d3–	= underachievement of sales goal for two-drawer files
	d4–	= underachievement of sales goal for three-drawer files
    
This is a goal programming problem since we are trying to satisfy multiple goals
so we should minimize the deviations from the goals considering the priorities
    
Minimize deviations
= P1d1– + P1d1+ + P2d2– + P3d3– + P3d4–

subject to
10X1 + 15X2 + d1– – d1+	 = $11,000 (profit target)
1X1 +     2X2	+ d2–	= 1,300 hours (production limit)
1X1		+ d3–	= 600 (two-drawer sales limit)
	 X2	+ d4–	= 400 (three-drawer sales limit)
All Xi, di variables >= 0


"""

import pulp


model = pulp.LpProblem("under/overachievement minimizing problem", pulp.LpMinimize)

x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')
d1_neg = pulp.LpVariable("d1_neg", lowBound=0, cat='Integer')
d1_plus = pulp.LpVariable("d1_plus", lowBound=0, cat='Integer')
d2_neg = pulp.LpVariable("d2_neg", lowBound=0, cat='Integer')
d3_neg = pulp.LpVariable("d3_neg", lowBound=0, cat='Integer')
d4_neg = pulp.LpVariable("d4_neg", lowBound=0, cat='Integer')


# Priorities 
p1 = 1
p2 = 2
p3 = 3




# Objective function
model += p1 * d1_neg + p1 * d1_plus + p2 * d2_neg + p3 * d3_neg + p3 * d4_neg, "under_over"
#model += d1_neg + d1_plus + d2_plus + d3_neg, "under_over"

# Constraints     
model += 10 * x1 + 15 * x2 + d1_neg - d1_plus == 11000.0  #(profit target)
model += x1 + 2* x2 + d2_neg                  == 1300   # (production limit hours)
model += x1 + d3_neg                          == 600.0   #(two-drawer sales limit)
model += x2 + d4_neg                          == 400.0   # (three-drawer sales limit)




# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( f"number of 2-drawer cabinets = {x1.varValue:.0f}")
print( f"number of 3-drawer cabinets = {x2.varValue:.0f}") 
print( f"underachievement of profit goal = {d1_neg.varValue}")
print( f"overachievement of profit goal  = {d1_plus.varValue}") 
print( f"undererachievement of idle time in production goal  = {d2_neg.varValue:.0f}")
print( f"underachievement of 2-drawer cabinet goal = {d3_neg.varValue:.0f}") 
print( f"underachievement of 3-drawer cabinet goal = {d4_neg.varValue:.0f}") 