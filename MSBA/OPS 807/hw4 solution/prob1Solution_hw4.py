# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:55:15 2019

@author: jg
"""

"""
WIN BIG CLUB

Club promotes gambling junkets to the Bahamas
$8,000 per week to spend on advertising
Goal is to reach the largest possible high-potential audience
Media types and audience figures shown below

MEDIUM	                            AUDIENCE COST  MAXIMUM ADS 
                                    REACHED PER AD  PER WEEK
                                    PER AD     
TV spot (1 minute)	                5,000	800		12
Daily newspaper (full-page ad)	    8,500	925		5
Radio spot (30 seconds, prime time)	2,400	290		25
Radio spot (1 minute, afternoon)	2,800	380		20


Place at least five radio spots per week
No more than $1,800 can be spent on radio advertising each week


	    X1 = number of 1-minute TV spots taken each week
		X2 = number of daily newspaper ads taken each week
		X3 = number of 30-second prime-time radio spots taken each week
		X4 = number of 1-minute afternoon radio spots taken each week
Objective:
	Maximize audience coverage = 5,000X1 + 8,500X2 + 2,400X3 + 2,800X4
	Subject to	
        X1	≤ 12	(max TV spots/wk)
		X2	≤ 5	(max newspaper ads/wk)
		X3	≤ 25	(max 30-sec radio spots/wk)
		X4	≤ 20	(max 1-min radio spots/wk)
		800X1 + 925X2 + 290X3 + 380X4	≤ $8,000	(weekly advertising budget)
		X3 + X4	≥ 5	(min radio spots contracted)
		290X3 + 380X4	≤ $1,800	(max dollars spent on radio)
		X1, X2, X3, X4	≥ 0


"""

import pulp 


model = pulp.LpProblem("maximizing problem", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Continuous')
x3 = pulp.LpVariable("x3", lowBound=0, cat='Continuous')
x4 = pulp.LpVariable("x4", lowBound=0, cat='Continuous')


# Objective function
model += 5000.0 * x1 + 8500.0 * x2 + 2400.0 * x3 + 2800.0 * x4, "maximize"



# Constraints     
model += x1 <= 12 
model += x2 <= 5 
model += x3 <= 25
model += x4 <= 20
model += 800. * x1 + 925. * x2 + 290. * x3 + 380. * x4 <= 8000.0
model += 290* x3 + 380 * x4 <= 1800
model += x3 + x4 >= 5


# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( f"Number of 1-minute TV spots = {x1.varValue}")
print( f"Number of daily newspaper ads = {x2.varValue}") 
print( f"Number of 30-second prime-time radio spots  = {x3.varValue}") 
print( f"Number of 1-minute afternoon radio spots = {x4.varValue}")
print(f'Total audience coverage is = ${pulp.value(model.objective)}')
