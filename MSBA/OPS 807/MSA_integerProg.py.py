# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 14:14:32 2019

@author: jg
"""

"""
MSA is a marketing research firm
Several requirements for a statistical validity
Survey at least 2,300 U.S. households
Survey at least 1,000 households whose heads are ≤ 30 years old
Survey at least 600 households whose heads are between 31 and 50
Ensure that at least 15% of those surveyed live in a state that borders Mexico
Ensure that no more than 20% of those surveyed who are 51 years of age or over live in a state that borders Mexico

MSA decides to conduct all surveys in person
Estimates of the costs of reaching people in each age and region category
Goal is to meet the sampling requirements at the least possible cost

Decision variables

X1 = number of 30 or younger and in a border state
X2 = number of 31-50 and in a border state
X3 = number 51 or older and in a border state
X4 = number 30 or younger and not in a border state
X5 = number of 31-50 and not in a border state
X6 = number 51 or older and not in a border state

Objective function

Minimize total interview costs = $7.50X1 + $6.80X2 + $5.50X3
                                 + $6.90X4 + $7.25X5 + $6.10X6

subject to:
    
X1 +	X2 +	X3 +	X4 +	X5 +	X6	≥	2,300	(total households)
	X1 +			X4			≥	1,000	(households 30 or younger)
		X2 +			X5		≥	600	(households 31-50)
	X1 +	X2 +	X3 				≥ 0.15(X1 + X2+ X3 + X4 + X5 + X6)   
									(border states)
			X3 				≤ 0.20(X3 + X6)	(limit on age group 
										51+ who can live 
										in border state)
		      X1, X2, X3, X4, X5, X6 	≥ 0


"""

"""
Solution using pulp
"""

from pulp import *



model = LpProblem("Profit minimising problem", LpMinimize)


x1 = LpVariable('x1', lowBound=0, cat='Integer')
x2 = LpVariable('x2', lowBound=0, cat='Integer')
x3 = LpVariable('x3', lowBound=0, cat='Integer')
x4 = LpVariable('x4', lowBound=0, cat='Integer')
x5 = LpVariable('x5', lowBound=0, cat='Integer')
x6 = LpVariable('x6', lowBound=0, cat='Integer')



# Objective function
model += 7.50*x1+6.80*x2+5.50*x3+6.90*x4+7.25*x5+6.10*x6 , "Cost"

# Constraints
model += x1+x2+x3+x4+x5+x6 >= 2300
model += x1 + x4           >= 1000
model += x2 + x5           >= 600
model += 0.85*x1+0.85*x2+0.85*x3-0.15*x4-0.15*x5-0.15*x6 >= 0 
model += 0.8*x3-0.2*x6     <= 0

# Solve our problem
model.solve()
LpStatus[model.status]

 

print(f'30 or younger: {x1.varValue}, {x2.varValue} \n31-50: {x2.varValue}, {x3.varValue} \nborder states: {x1.varValue}, {x2.varValue}, {x3.varValue} \nborder > 51: {x3.varValue}, {x6.varValue}')
print(f'Total cost is = ${value(model.objective)}')

"""
Solution with Gurobi
"""
import gurobipy as gby

#try:

# Create a new model
m = gby.Model("mip1")

# Create variables
x1 = m.addVar(vtype=gby.GRB.INTEGER, name="x1")
x2 = m.addVar(vtype=gby.GRB.INTEGER, name="x2")
x3 = m.addVar(vtype=gby.GRB.INTEGER, name="x3")
x4 = m.addVar(vtype=gby.GRB.INTEGER, name="x4")
x5 = m.addVar(vtype=gby.GRB.INTEGER, name="x5")
x6 = m.addVar(vtype=gby.GRB.INTEGER, name="x6")

# Set objective
m.setObjective(7.50*x1+6.80*x2+5.50*x3+6.90*x4+7.25*x5+6.10*x6 , gby.GRB.MINIMIZE)

# Add constraint:x1+x2+x3+x4+x5+x6 >= 2300
m.addConstr(x1+x2+x3+x4+x5+x6 >= 2300, "c0")

# Add constraint: x1 + x4 >= 1000
m.addConstr(x1 + x4 >= 1000, "c1")

# Add constraint: x2 + x5 >= 600
m.addConstr(x2 + x5 >= 600, "c2")

# Add constraint: 0.85*x1+0.85*x2+0.85*x3-0.15*x4-0.15*x5-0.15*x6 >= 0
m.addConstr(0.85*x1+0.85*x2+0.85*x3-0.15*x4-0.15*x5-0.15*x6 >= 0 , "c3")

# Add constraint: 0.8*x3-0.2*x6 <= 0
m.addConstr(0.8*x3-0.2*x6 <= 0, "c4")



# Optimize model
m.optimize()
print()
for v in m.getVars():
    print(f'{v.varName} : {v.x:.0f}')

print()
print(f'Obj: {m.objVal}')

#except gby.GurobiError as e:
#    print('Error code ' + str(e.errno) + ": " + str(e))

#except AttributeError:
#    print('Encountered an attribute error')

