# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:06:47 2019

@author: jg
"""

"""
Hong Kong Bank of Commerce and Industry requires between 10 and 18 tellers depending on the time of day
The bank wants a schedule that will minimize total personnel costs
Lunch time from noon to 2 pm is generally the busiest
Bank employs 12 full-time tellers, many part-time workers

Part-time workers must put in exactly four hours per day, can start anytime between 9 am and 1 pm, and are inexpensive
Full-time workers work from 9 am to 3 pm and have 1 hour for lunch
Part-time hours are limited to a maximum of 50% of the day’s total requirements
Part-timers earn $8 per hour on average
Full-timers earn $100 per day on average
It will release one or more of its full-time tellers if it is profitable to do so

Labor requirements:
    
TIME PERIOD	         NUMBER OF TELLERS REQUIRED
9 am – 10 am	           10
10 am – 11 am	           12
11 am – Noon	           14
Noon – 1 pm	               16
1 pm – 2 pm	               18
2 pm – 3 pm	               17
3 pm – 4 pm	               15
4 pm – 5 pm	               10

decision variables:
    
	F	= full-time tellers
	P1	= part-timers starting at 9 am (leaving at 1 pm)
	P2	= part-timers starting at 10 am (leaving at 2 pm)
	P3	= part-timers starting at 11 am (leaving at 3 pm)
	P4	= part-timers starting at noon (leaving at 4 pm)
	P5	= part-timers starting at 1 pm (leaving at 5 pm)

Objective function:
    Minimize
    total perosnel cost    = $100F + $32(P1 + P2 + P3 + P4 + P5)

Constraints:
    
F	+ P1					≥	10
F	+ P1	+ P2				≥	12
0.5F	+ P1	+ P2	+ P3			≥	14
0.5F	+ P1	+ P2	+ P3	+ P4		≥	16
F		+ P2	+ P3	+ P4	+ P5	≥	18
F			+ P3	+ P4	+ P5	≥	17
F				+ P4	+ P5	≥	15
F					+ P5	≥	10
F						≤	12
	4P1	+ 4P2	+ 4P3	+ 4P4	+ 4P5	≤	0.50(112)
F, P1, P2, P3, P4, P5	≥	0
    
"""

import pulp 


model = pulp.LpProblem("minimization problem", pulp.LpMinimize)

F = pulp.LpVariable("F", lowBound=0, cat='Integer')
P1 = pulp.LpVariable("P1", lowBound=0, cat='Integer')
P2 = pulp.LpVariable("P2", lowBound=0, cat='Integer')
P3 = pulp.LpVariable("P3", lowBound=0, cat='Integer')
P4 = pulp.LpVariable("P4", lowBound=0, cat='Integer')
P5 = pulp.LpVariable("P5", lowBound=0, cat='Integer')


# Objective function
model += 100 * F + 32 * (P1 + P2 + P3 + P4 + P5), "minimize"

    

# Constraints     
model += F + P1 >= 10 
model += F + P1 + P2 >= 12 
model += 0.5* F + P1 + P2 + P3 >= 14 
model += 0.5* F + P1 + P2 + P3 + P4 >= 16
model += F + P1 + P2 + P3 + P4 + P5 >= 18
model += F + P3 + P4 + P5 >= 17
model += F + P4 + P5 >= 15
model += F + P5 >= 10
model += F  <= 12
model += 4* (P1 + P2 + P3 + P4 + P5) <= 0.5*(112)


# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( f"Number of full-time Employees = {F.varValue:.0f}")
print( f"Number of part-timers starting at 9 am = {P1.varValue:.0f}") 
print( f"Number of part-timers starting at 10 am  = {P2.varValue:.0f}") 
print( f"Number part-timers starting at 11 am = {P3.varValue:.0f}")
print( f"Number part-timers starting at 12 pm = {P4.varValue:.0f}")
print( f"Number part-timers starting at 1 pm = {P5.varValue:.0f}")
print(f'Total Cost is = ${pulp.value(model.objective)}')
