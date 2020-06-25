# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 14:33:16 2019

@author: jg
"""
"""
Find the shortest distance from one location to another
Can be modeled as
– A linear programming problem with 0-1 variables
(A special type of transshipment problem)
– Using specialized algorithm (Dijkstra algorithm is one solution)

A famous problem in this case is the travelling salesman problem (TSP)

Ray Design transports beds, chairs, and other furniture items from the factory to the warehouse
– Travel through several cities
– No direct interstate highways

Find the route with the shortest distance

Variables
Xij= 1 if arc from node ito node jis selected and Xij= 0 otherwise
where
i= 1, 2, 3, 4, 5
j= 2, 3, 4, 5, 6
Constraints specify the number of units going into a node must equal the number of units going out of the node

Variables
Xij= 1 if arc from node ito node jis selected and Xij= 0 otherwise
where
i= 1, 2, 3, 4, 5
j= 2, 3, 4, 5, 6
Constraints specify the number of units going into a node must equal the number of units going out of the node


Origin point must ship one unit
X12+ X13= 1
Final destination must have one unit shipped into it
X46+ X56= 1
Intermediate nodes must have same amounts entering and leaving
X12+ X32= X23+ X24+ X25
or
X12+ X32–X23–X24–X25= 0


Minimize distance =100X12+ 200X13+ 50X23+ 50X32+ 200X24+ 200X42+ 100X25 \
+ 100X52+ 40X35+ 40X53+ 150X45+ 150X54+ 100X46+ 100X56

subject to

X12+ X13 = 1 Node 1
X12+ X32–X23–X24–X25 = 0 Node 2
X13+ X23–X32–X35 = 0 Node 3
X24+ X54–X42–X45–X46 = 0 Node 4
X25+ X35+ X45–X52–X53–X54–X56 = 0 Node 5
X46+ X56 = 1 Node 6
All variables = 0 or 1
"""

import pulp  


"""
Solving using pulp library for integer/binary programming 

"""
model = pulp.LpProblem("Assignment problem", pulp.LpMinimize)


X12 = pulp.LpVariable("X12", lowBound=0, cat='Binary')
X13 = pulp.LpVariable("X13", lowBound=0, cat='Binary')
X21 = pulp.LpVariable("X21", lowBound=0, cat='Binary')
X23 = pulp.LpVariable("X23", lowBound=0, cat='Binary')
X32 = pulp.LpVariable("X32", lowBound=0, cat='Binary')
X24 = pulp.LpVariable("X24", lowBound=0, cat='Binary')
X42 = pulp.LpVariable("X42", lowBound=0, cat='Binary')
X25 = pulp.LpVariable("X25", lowBound=0, cat='Binary')
X52 = pulp.LpVariable("X52", lowBound=0, cat='Binary')
X35 = pulp.LpVariable("X35", lowBound=0, cat='Binary')
X53 = pulp.LpVariable("X53", lowBound=0, cat='Binary')
X45 = pulp.LpVariable("X45", lowBound=0, cat='Binary')
X54 = pulp.LpVariable("X54", lowBound=0, cat='Binary')
X46 = pulp.LpVariable("X46", lowBound=0, cat='Binary')
X56 = pulp.LpVariable("X56", lowBound=0, cat='Binary')



# Objetive function
model += 100*X12+ 200*X13+ 50*X23+ 50*X32+ 200*X24+ 200*X42+ 100*X25 \
+ 100*X52+ 40*X35+ 40*X53+ 150*X45+ 150*X54+ 100*X46+ 100*X56



# constraints
# Node 1
model += X12 + X13 == 1
#Node 2
model += X12+ X32 == X23 + X24 + X25 
#Node 3
model += X13+ X23 == X32 + X35
#Node 4
model += X24 + X54 == X42 + X45 + X46
#Node 5
model += X25+ X35 + X45 == X52 + X53 + X54 + X56
# Node 6
model += X46 + X56 == 1


# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values

print(f'from node 1 to 2  = {X12.varValue:.0f}')
print(f'from node 1 to  3 = {X13.varValue:.0f}') 
print(f'from node 2 to  3 = {X23.varValue:.0f}')
print(f'from node 2 to  4 = {X24.varValue:.0f}')
print(f'from node 2 to  5 = {X25.varValue:.0f}')
print(f'from node 3 to  5 = {X35.varValue:.0f}')
print(f'from node 3 to 2 = {X32.varValue:.0f}')
print(f'from node 4 to 2 = {X42.varValue:.0f}')
print(f'from node 4 to 5 = {X45.varValue:.0f}')
print(f'from node 4 to 6 = {X46.varValue:.0f}')
print(f'from node 5 to 3 = {X53.varValue:.0f}')
print(f'from node 5 to 4 = {X54.varValue:.0f}')
print(f'from node 5 to 6 = {X56.varValue:.0f}')
print(f'Minimum distance/shortest path is = {pulp.value(model.objective)} miles')

