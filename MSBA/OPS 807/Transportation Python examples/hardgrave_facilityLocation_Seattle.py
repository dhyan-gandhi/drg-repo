# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:23:50 2019

Facility location problem. 
Case study: Hardgrave Machine Company

@author: jg
"""
"""
Hardgrave Machine Company produces computer components in Cincinnati, Salt Lake City, and Pittsburgh
Four warehouses in Detroit, Dallas, New York, and Los Angeles
Two new plant sites being considered –Seattle and Birmingham
Which of the new locations will yield the lowest cost for the firm in combination with the existing plants and warehouses?

Assumptions:
    
Xij=number of units shipped from source ito destination j
Where
i=1, 2, 3, 4 with 1 = Cincinnati, 2 = Salt Lake City, 3 = Pittsburgh, and 4 = Seattle
j=1, 2, 3, 4 with 1 = Detroit, 2 = Dallas, 3 = New York, and 4 = Los Angeles

Objective function:

    Minimize total cost =73X11+ 103X12+ 88X13+ 108X14+ 85X21+ 80X22+ 100X23
                         + 90X24+ 88X31+ 97X32+ 78X33+ 118X34+ 113X41+ 91X42
                         + 118X43+ 80X44

Subject to:
X11+ X21+ X31+ X41= 10,000 Detroit demand
X12+ X22+ X32+ X42= 12,000 Dallas demand
X13+ X23+ X33+ X43= 15,000 New York demand
X14+ X24+ X34+ X44= 9,000 Los Angeles demand
X11+ X12+ X13+ X14≤ 15,000 Cincinnati supply
X21+ X22+ X23+ X24≤ 6,000 Salt Lake City supply
X31+ X32+ X33+ X34≤ 14,000 Pittsburgh supply
X41+ X42+ X43+ X44≤ 11,000 Seattle supply
All variables Xij≥ 0


"""
import pulp


model = pulp.LpProblem("minimizing transportation cost problem", pulp.LpMinimize)

X11 = pulp.LpVariable("X11", lowBound=0, cat='Continuous')
X12 = pulp.LpVariable("X12", lowBound=0, cat='Continuous')
X13 = pulp.LpVariable("X13", lowBound=0, cat='Continuous')
X14 = pulp.LpVariable("X14", lowBound=0, cat='Continuous')
X21 = pulp.LpVariable("X21", lowBound=0, cat='Continuous')
X22 = pulp.LpVariable("X22", lowBound=0, cat='Continuous')
X23 = pulp.LpVariable("X23", lowBound=0, cat='Continuous')
X24 = pulp.LpVariable("X24", lowBound=0, cat='Continuous')
X31 = pulp.LpVariable("X31", lowBound=0, cat='Continuous')
X32 = pulp.LpVariable("X32", lowBound=0, cat='Continuous')
X33 = pulp.LpVariable("X33", lowBound=0, cat='Continuous')
X34 = pulp.LpVariable("X34", lowBound=0, cat='Continuous')
X41 = pulp.LpVariable("X41", lowBound=0, cat='Continuous')
X42 = pulp.LpVariable("X42", lowBound=0, cat='Continuous')
X43 = pulp.LpVariable("X43", lowBound=0, cat='Continuous')
X44 = pulp.LpVariable("X44", lowBound=0, cat='Continuous')


#Minimize total cost including Seattle =73X11+ 103X12+ 88X13+ 108X14+ 85X21+ 80X22+ 100X23
#                         + 90X24+ 88X31+ 97X32+ 78X33+ 118X34+ 113X41+ 91X42
#                         + 118X43+ 80X44

# Objective function Seattle
model += 73*X11 +  103*X12 + 88*X13 + 108*X14 + 85*X21 + 80*X22 + 100*X23 + 90*X24 \
          + 88*X31 +97*X32 + 78*X33 + 118*X34 + 113*X41 + 91*X42+118*X43+80*X44, "transportation cost minimization"

# Constraints Seattle case
          
model += X11+ X21+ X31+ X41== 10000 #Detroit demand
model += X12+ X22+ X32+ X42== 12000 #Dallas demand
model += X13+ X23+ X33+ X43== 15000 #New York demand
model += X14+ X24+ X34+ X44== 9000 #Los Angeles demand
model += X11+ X12+ X13+ X14<= 15000 #Cincinnati supply
model += X21+ X22+ X23+ X24<= 6000 #Salt Lake City supply
model += X31+ X32+ X33+ X34<= 14000 #Pittsburgh supply
model += X41+ X42+ X43+ X44<= 11000 #Seattle supply



# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( f"from Cincinnati to Detroit  = {X11.varValue}")
print( f"from Cincinnati to Dallas  = {X12.varValue}") 
print( f"from Cincinnati to New York   = {X13.varValue}") 
print( f"from Cincinnati to Los Angeles   = {X14.varValue}") 
print( f"from Salt Lake City to Detroit = {X21.varValue}")
print( f"from Salt Lake City to Dallas  = {X22.varValue}") 
print( f"from Salt Lake City to New York  = {X23.varValue}")
print( f"from Salt Lake City to Los Angeles  = {X24.varValue}")
print( f"from Pittsburgh to Detroit = {X31.varValue}") 
print( f"from Pittsburgh to Dallas = {X32.varValue}") 
print( f"from Pittsburgh to New York = {X33.varValue}")
print( f"from Pittsburgh to Los Angeles = {X34.varValue}") 
print( f"from Seattle to Detroit = {X41.varValue}") 
print( f"from Seattle to Dallas = {X42.varValue}") 
print( f"from Seattle to New York = {X43.varValue}")
print( f"from Seattle to Los Angeles = {X44.varValue}") 
print(f'Total Cost is = ${pulp.value(model.objective)}')