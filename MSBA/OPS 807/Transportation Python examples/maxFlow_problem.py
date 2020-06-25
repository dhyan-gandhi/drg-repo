# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:41:10 2019

Maximal Flow problem

@author: jg
"""
"""
Determine maximum number of cars from east to west for Waukesha WI road system

Variables
Xij= flow from node into node j
where
i= 1, 2, 3, 4, 5, 6
j= 1, 2, 3, 4, 5, 6
Constraints necessary for
–
Capacity of each arc
–
Equal flows into and out of each arc

Maximize flow = X61
subject to

Capacities for arcs from node 1
X12 ≤ 3
X13 ≤ 10
X14 ≤ 2

Capacities for arcs from node 2
X21 ≤ 1
X24 ≤ 1
X26 ≤ 2

Capacities for arcs from node 3
X34 ≤ 3
X35 ≤ 2

Capacities for arcs from node 4
X42 ≤ 1
X43 ≤ 1
X46 ≤ 1

Capacities for arcs from node 5
X53 ≤ 1
X56 ≤ 1

Capacities for arcs from node 6
X62 ≤ 2
X64 ≤ 1

Flows into = flows out of node 1
(X21+ X61) –(X12+ X13+ X14) = 0
Flows into = flows out of node 2
(X12+ X42+ X62) –(X21+X24+ X26) = 0
Flows into = flows out of node 3
(X13+ X43+ X53) –(X34+ X35) = 0
Flows into = flows out of node 4
(X14+ X24+ X34+ X64) –(X42+ X43+ X46) = 0
Flows into = flows out of node 5
(X35) –(X56+ X53) = 0
Flows into = flows out of node 6
(X26+ X46+ X56) –(X61+ X62+ X64) = 0

Xij ≥ 0
"""
import pulp


model = pulp.LpProblem("maximizing flow problem", pulp.LpMaximize)


X12 = pulp.LpVariable("X12", lowBound=0, cat='Integer')
X13 = pulp.LpVariable("X13", lowBound=0, cat='Integer')
X14 = pulp.LpVariable("X14", lowBound=0, cat='Integer')
X21 = pulp.LpVariable("X21", lowBound=0, cat='Integer')
X24 = pulp.LpVariable("X24", lowBound=0, cat='Integer')
X26 = pulp.LpVariable("X26", lowBound=0, cat='Integer')
X34 = pulp.LpVariable("X34", lowBound=0, cat='Integer')
X35 = pulp.LpVariable("X35", lowBound=0, cat='Integer')
X42 = pulp.LpVariable("X42", lowBound=0, cat='Integer')
X43 = pulp.LpVariable("X43", lowBound=0, cat='Integer')
X46 = pulp.LpVariable("X46", lowBound=0, cat='Integer')
X53 = pulp.LpVariable("X53", lowBound=0, cat='Integer')
X56 = pulp.LpVariable("X56", lowBound=0, cat='Integer')
X61 = pulp.LpVariable("X61", lowBound=0, cat='Integer')
X62 = pulp.LpVariable("X62", lowBound=0, cat='Integer')
X64 = pulp.LpVariable("X64", lowBound=0, cat='Integer')



# the objective function stays the same except for X4x coefficients, i.e. X41,....
# the total cost is shipping cost + production cost 
# shipping cost for Birmingham = [$35, $30, $41, $50] + production cost at Birmingham  = $49
#Minimize total cost =73X11+ 103X12+ 88X13+ 108X14+ 85X21+ 80X22+ 100X23
#                         + 90X24+ 88X31+ 97X32+ 78X33+ 118X34+ 84X41+ 79X42
#                         + 90X43+ 99X44

# Objective function Birmingham
model += X61, "maximum flow problem"

# Constraints 
model += X12 <= 3
model += X13 <= 10
model += X14 <= 2

#Capacities for arcs from node 2
model += X21 <= 1
model += X24 <= 1
model += X26 <= 2

#Capacities for arcs from node 3
model += X34 <= 3
model += X35 <= 2

#Capacities for arcs from node 4
model += X42 <= 1
model += X43 <= 1
model += X46 <= 1

#Capacities for arcs from node 5
model += X53 <= 1
model += X56 <= 1

#Capacities for arcs from node 6
model += X62 <= 2
model += X64 <= 1

model += X21 + X61 == X12 + X13 + X14   #Flows into = flows out of node 1
model += X12+ X42+ X62 == X21+X24+ X26      #Flows into = flows out of node 2
model += (X13+ X43+ X53) == (X34+ X35)   #Flows into = flows out of node 3
model += (X14+ X24+ X34+ X64) == (X42+ X43+ X46) #Flows into = flows out of node 4
model += (X35) == (X56+ X53)   #Flows into = flows out of node 5
model += (X26+ X46+ X56) == (X61+ X62+ X64) #Flows into = flows out of node 6


# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( f"flow from node 1 to 2  = {X12.varValue:.0f}") 
print( f"flow from node 1 to 3   = {X13.varValue:.0f}") 
print( f"flow from node 1 to 4   = {X14.varValue:.0f}") 
print( f"flow from node 2 to 1  = {X21.varValue:.0f}")
print( f"flow from node 2 to 6   = {X26.varValue:.0f}")
print( f"flow from node 2 to 4  = {X24.varValue:.0f}")
print( f"flow from node 3 to 4  = {X34.varValue:.0f}") 
print( f"flow from node 3 to 5  = {X35.varValue:.0f}") 
print( f"flow from node 4 to 2 = {X42.varValue:.0f}") 
print( f"flow from node 4 to 3 = {X43.varValue:.0f}")
print( f"flow from node 4 to 6 = {X46.varValue:.0f}")
print( f"flow from node 5 to 3 = {X53.varValue:.0f}") 
print( f"flow from node 5 to 6 = {X56.varValue:.0f}")
print( f"flow from node 6 to 1 = {X61.varValue:.0f}") 
print( f"flow from node 6 to 2 = {X62.varValue:.0f}")  
print( f"flow from node 6 to 4 = {X64.varValue:.0f}")   
print(f'Maximum flow from source to destination = {pulp.value(model.objective):.0f}')

