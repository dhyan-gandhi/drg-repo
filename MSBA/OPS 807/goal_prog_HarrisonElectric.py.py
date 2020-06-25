# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 23:59:35 2018

@author: jahan


 problem statement
Company produces two products, old-fashioned chandeliers and ceiling fans
Both require a two-step production process involving wiring and assembly
It takes about 2 hours to wire each chandelier and 3 hours to wire a ceiling fan
Final assembly of the chandeliers and fans requires 6 and 5 hours, respectively
Only 12 hours of wiring time and 30 hours of assembly time are available
Each chandelier produced nets the firm $7 and each fan $6

Single-goal programming formulation

Minimize under or
overachievement     =  d1– + d1+
of profit target

subject to
 	$7X1 +	$6X2	+ d1– – d1+	=	$30	(profit goal constraint) 
     pay attention that our previous objective function is now a constraint and 
     the new objective function is to minimize under or overachievement
     
	2X1 +	3X2				≤	12	(wiring hours)
	6X1 +	5X2				≤	30	(assembly hours)
			X1, X2, d1–, d1+	≥	0

where
		X1 = number of chandeliers produced 
		X2 = number of ceiling fans produced
        
        
"""        

import pulp



"""
Solving using pulp library for goal programming 

"""
model = pulp.LpProblem("under/overachievement minimizing problem", pulp.LpMinimize)

x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')
d1_neg = pulp.LpVariable("d1_neg", lowBound=0, cat='Integer')
d1_plus = pulp.LpVariable("d1_plus", lowBound=0, cat='Integer')

# Objective function
model += d1_neg + d1_plus, "under_over"

# Constraints

model += 2 * x1 + 3 * x2 <= 12
model += 6 * x1 + 5 * x2 <= 30
model += 7 * x1 + 6 * x2 + d1_neg - d1_plus == 30


# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( "Number of chandeliers produced = {}".format(x1.varValue))
print( "Number of ceiling fans produced = {}".format(x2.varValue)) 
print( "Underachievement of Target Profit = {}".format(d1_neg.varValue))
print( "Overachievement of Target Profit = {}".format(d1_plus.varValue)) 





