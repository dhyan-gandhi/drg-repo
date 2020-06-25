# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:13:14 2019
LP with Binary decision variables and dependent selection
@author: jg
"""

"""
Simkin, Simkin, and Steinberg specialize in recommending oil stock portfolios
One client has the following specifications:
    
    - At least two Texas firms must be in the portfolio
    - No more than one investment can be made in a foreign oil company
    - One of the two California oil stocks must be purchased
    - The client has $3 million to invest and wants to buy large blocks of shares

Formulation:
    
Maximize return =	50X1 + 80X2 + 90X3 + 120X4 + 110X5 + 40X6 + 75X7 

Limiting the Number of Alternatives Selected and Dependent Selections 
subject to
	X1 +	X4 +	X5	≥	2	(Texas constraint)
		     X2  +	X3	≤	1	(foreign oil constraint) 
		     X6  +	X7	=	1	(California constraint)
   480X1 + 540X2 + 680X3 + 1,000X4 + 700X5 + 510X6 + 900X7	  ≤	3,000	                                                                           ($3 million limit)
			Xi	=	0 or 1 for all i


"""

from pulp import *



model = LpProblem("ROI maximising problem", LpMaximize)

#constUpBnd = 20000

x1 = LpVariable('x1', lowBound=0, cat='Binary')
x2 = LpVariable('x2', lowBound=0,  cat='Binary')
x3 = LpVariable('x3', lowBound=0,  cat='Binary')
x4 = LpVariable('x4', lowBound=0,  cat='Binary')
x5 = LpVariable('x5', lowBound=0, cat='Binary')
x6 = LpVariable('x6', lowBound=0,  cat='Binary')
x7 = LpVariable('x7', lowBound=0,  cat='Binary')



# Objective function
model += 50*x1 + 80*x2 + 90*x3 + 120*x4 + 110*x5 + 40*x6 + 75*x7, "ROI" 

# Constraints
model += x1 + x4 + x5 >= 2	#(Texas constraint)
model += x2 + x3 	<=	1	#(foreign oil constraint)
model += x6 + x7	==	1	#(California constraint)
model += 480*x1 + 540*x2 + 680*x3 + 1000*x4 + 700*x5 + 510*x6 + 900*x7 <= 3000	#total available investement in ($1000)


# Solve our problem
model.solve()
LpStatus[model.status]

"""
Optimal solution will result in a profit of $360,000
x1=x2=x3=0, x3=x4=x5=x6 =1

"""
 

print(f'x1: {x1.varValue:.0f}, x2: {x2.varValue:.0f}, x3: {x3.varValue:.0f}, x4: {x4.varValue:.0f}, x5: {x5.varValue:.0f}, x6: {x6.varValue:.0f}, x7: {x7.varValue:.0f}')
print(f'ROI ($1000) = ${value(model.objective):.2f}')

"""
Solution with Gurobi
"""
import gurobipy as gby

try:

    # Create a new model
    m = gby.Model("mip")

    # Create variables
    x1 = m.addVar(vtype=gby.GRB.BINARY, name="x1")
    x2 = m.addVar(vtype=gby.GRB.BINARY, name="x2")
    x3 = m.addVar(vtype=gby.GRB.BINARY, name="x3")
    x4 = m.addVar(vtype=gby.GRB.BINARY, name="x4")
    x5 = m.addVar(vtype=gby.GRB.BINARY, name="x5")
    x6 = m.addVar(vtype=gby.GRB.BINARY, name="x6")
    x7 = m.addVar(vtype=gby.GRB.BINARY, name="x7")
    # Set objective
    m.setObjective(50*x1 + 80*x2 + 90*x3 + 120*x4 + 110*x5 + 40*x6 + 75*x7 , gby.GRB.MAXIMIZE)


	#total available investement 10^6/1000
    # Add constraint0.125*x1 + 0.066*x4 <= 1200
    m.addConstr(x1 + x4 + x5 >= 2, "c0")

    # Add constraint: 0.08*x2 + 0.05*x3 <=	3000
    m.addConstr(x2 + x3 	<=	1, "c1")

    # Add constraint:0.05*x3 + 0.44*x4	<=	1600
    m.addConstr(x6 + x7	==	1, "c2")
    
    # add constraint: 480*x1 + 540*x2 + 680*x3 + 1000*x4 + 700*x5 + 510*x6 + 900*x7 <= 3000
    m.addConstr(480*x1 + 540*x2 + 680*x3 + 1000*x4 + 700*x5 + 510*x6 + 900*x7 <= 3000, "c3")
    
    
    # Optimize model
    m.optimize()
    print()
    for v in m.getVars():
        print(f'{v.varName} : {v.x:.0f}')

    print()
    print(f'Obj IN ($1000): {m.objVal:.2f}')
    """
    Optimal solution will result in a profit of $360,000
    x1=x2=x3=0, x3=x4=x5=x6 =1

    """
except gby.GurobiError as e:
    print('Error code ' + str(e.errno) + ": " + str(e))

except AttributeError:
    print('Encountered an attribute error')
