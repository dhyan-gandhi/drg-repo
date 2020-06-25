# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:16:32 2019

Items are being moved from a source to a destination through an intermediate point (a transshipment point)
Transshipment problem

@author: jg
"""

"""
Frosty Machines manufactures snow blowers in Toronto and Detroit
Shipped to regional distribution centers in Chicago and Buffalo
Then shipped to supply houses in New York, Philadelphia, and St. Louis
Shipping costs vary by location and destination
Snow blowers cannot be shipped directly from the factories to the supply houses

Minimize transportation costs associated with shipping
snow blowers subject to demands and supplies

Minimize cost subject to
1.The number of units shipped from Toronto is not more than 800
2.The number of units shipped from Detroit is not more than 700
3.The number of units shipped to New York is 450
4.The number of units shipped to Philadelphia is 350
5.The number of units shipped to St. Louis is 300
6.The number of units shipped out of Chicago is equal to the number of units shipped into Chicago
7.The number of units shipped out of Buffalo is equal to the number of units shipped into Buffalo

    
Decision variables
Xij=number of units shipped from location (node)i to location (node) j
where
i= 1, 2, 3, 4
j= 3, 4, 5, 6, 7

Objective function:

Minimize cost =4X13+ 7X14+ 5X23+ 7X24+ 6X35+ 4X36+ 5X37+ 2X45+ 3X46+ 4X47

subject to
X13+ X14≤ 800(Supply at Toronto [node 1])
X23+ X24≤ 700(Supply at Detroit [node 2])
X35+ X45= 450(Demand at New York [node 5])
X36+ X46= 350(Demand at Philadelphia [node 6])
X37 + X47= 300(Demand at St. Louis [node 7])
X13+ X23= X35+ X36+ X37(Shipping through Chicago [node 3])
X14+ X24= X45+ X46+X47(Shipping through Buffalo [node 4])
Xij≥ 0 for all iand j(nonnegativity)



"""
import pulp


model = pulp.LpProblem("minimizing transportation cost problem", pulp.LpMinimize)


X13 = pulp.LpVariable("X13", lowBound=0, cat='Continuous')
X14 = pulp.LpVariable("X14", lowBound=0, cat='Continuous')
X23 = pulp.LpVariable("X23", lowBound=0, cat='Continuous')
X24 = pulp.LpVariable("X24", lowBound=0, cat='Continuous')
X35 = pulp.LpVariable("X35", lowBound=0, cat='Continuous')
X36 = pulp.LpVariable("X36", lowBound=0, cat='Continuous')
X37 = pulp.LpVariable("X37", lowBound=0, cat='Continuous')
X45 = pulp.LpVariable("X45", lowBound=0, cat='Continuous')
X46 = pulp.LpVariable("X46", lowBound=0, cat='Continuous')
X47 = pulp.LpVariable("X47", lowBound=0, cat='Continuous')


#Minimize cost =4X13+ 7X14+ 5X23+ 7X24+ 6X35+ 4X36+ 5X37+ 2X45+ 3X46+ 4X47

# Objective function Birmingham
model += 4*X13+ 7*X14+ 5*X23+ 7*X24+ 6*X35+ 4*X36+ 5*X37+ 2*X45+ 3*X46+ 4*X47, "transportation cost minimization"

# Constraints Seattle case

model += X13+ X14  <= 800 #(Supply at Toronto [node 1])
model += X23+ X24  <= 700 #(Supply at Detroit [node 2])
model += X35+ X45  == 450 #(Demand at New York [node 5])
model += X36+ X46  == 350 #(Demand at Philadelphia [node 6])
model += X37 + X47 == 300 #(Demand at St. Louis [node 7])
model += X13+ X23  == X35+ X36+ X37 #(Shipping through Chicago [node 3])
model += X14+ X24  == X45+ X46+ X47 #(Shipping through Buffalo [node 4])

          
# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values

print( f"from Toronto to Chicago   = {X13.varValue}") 
print( f"from Toronto to Buffalo   = {X14.varValue}") 
print( f"from Detroit to Chicago  = {X23.varValue}")
print( f"from Detroit to Buffalo  = {X24.varValue}")
print( f"from Chicago to NEW YORK = {X35.varValue}") 
print( f"from Chicago to Philadelphia = {X36.varValue}") 
print( f"from Chicago to St.Louis = {X37.varValue}")
print( f"from Buffalo to NEW YORK = {X45.varValue}") 
print( f"from Buffalo to Philadelphia = {X46.varValue}") 
print( f"from Buffalo to St.Louis = {X47.varValue}")
print(f'Total Cost is = ${pulp.value(model.objective)}')