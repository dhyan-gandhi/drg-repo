# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:26:24 2019

@author: jg
"""

"""
10-19.  

a.  Let Xij = 1 if generator i is functioning during time period j, and 0 
otherwise; where i = 1, 2, 3 and 
j = 1 for 6–2 time period; j = 2 for 2–10 time period; j = 3 for 6–10 time period.

Let Yij = megawatts produced by generator i in time period j, where i = 1, 2, 3 
and j = 1 for 6–2 time period; j = 2 for 2–10 time period.

Minimize cost = 6,000(X11 + X12 + X13) + 5,000(X21 + X22 + X23) + 4,000(X31 + X32 + X33) 
+ 8(Y11 + Y12) + 9(Y21 + Y22) + 7(Y31 + Y32)

Subject to:
    
Y11 + Y21 + Y31 >= 3,200	megawatts requirements from 6–2
Y12 + Y22 + Y32 >= 5,700	megawatts requirements from 2–10
Y11 <= 2,400(X11 + X13)	maximum megawatts from #1 from 6–2
Y12 <= 2,400(X12 + X13)	maximum megawatts from #1 from 2–10
Y21 <= 2,100(X21 + X23)	maximum megawatts from #2 from 6–2
Y22 <= 2,100(X22 + X23)	maximum megawatts from #2 from 2–10
Y31 <= 3,300(X31 + X33)	maximum megawatts from #3 from 6–2
Y32 <= 3,300(X32 + X33)	maximum megawatts from #3 from 2–10
X11 + X12 + X13 <= 1	generator #1 starts up at most once
X21 + X22 + X23 <= 1	generator #2 starts up at most once
X31 + X32 + X33 <= 1	generator #3 starts up at most once
Xij = 0 or 1 for all i, j
Yij >= 0 for all i, j


b.  The solution is: X13 = 1, X33 = 1, Y12 = 2,400, Y31 = 3,200, Y32 = 3,300, total cost = $74,700.
Thus, generator #1 will be utilized in the period 2–10 and will generate 2,400 megawatts of electricity. 
Generator #3 will be started at 6 and utilized for the entire 16 hours. 
It will generate 3,200 megawatts during the 6–2 time period, and 3,300 megawatts during the 2–10 time period.


"""

import pulp 


model = pulp.LpProblem("minimization problem", pulp.LpMinimize)

X11 = pulp.LpVariable("X11", lowBound=0, cat='Binary')
X12 = pulp.LpVariable("X12", lowBound=0, cat='Binary')
X13 = pulp.LpVariable("X13", lowBound=0, cat='Binary')
X21 = pulp.LpVariable("X21", lowBound=0, cat='Binary')
X22 = pulp.LpVariable("X22", lowBound=0, cat='Binary')
X23 = pulp.LpVariable("X23", lowBound=0, cat='Binary')
X31 = pulp.LpVariable("X31", lowBound=0, cat='Binary')
X32 = pulp.LpVariable("X32", lowBound=0, cat='Binary')
X33 = pulp.LpVariable("X33", lowBound=0, cat='Binary')

Y11 = pulp.LpVariable("Y11", lowBound=0, cat='Continuous')
Y12 = pulp.LpVariable("Y12", lowBound=0, cat='Continuous')
#Y13 = pulp.LpVariable("Y13", lowBound=0, cat='Continuous')
Y21 = pulp.LpVariable("Y21", lowBound=0, cat='Continuous')
Y22 = pulp.LpVariable("Y22", lowBound=0, cat='Continuous')
#Y23 = pulp.LpVariable("Y23", lowBound=0, cat='Continuous')
Y31 = pulp.LpVariable("Y31", lowBound=0, cat='Continuous')
Y32 = pulp.LpVariable("Y32", lowBound=0, cat='Continuous')
Y33 = pulp.LpVariable("Y33", lowBound=0, cat='Continuous')

# Objective function
model += 6000 * (X11 + X12 + X13) + 5000 * (X21 + X22 + X23) \
+ 4000 * (X31 + X32 + X33) + 8*(Y11 + Y12) + 9*(Y21 + Y22) + 7*(Y31 + Y32)



# Constraints     
model += Y11 + Y21 + Y31 >= 3200	# megawatts requirements from 6–2
model += Y12 + Y22 + Y32 >= 5700	# megawatts requirements from 2–10
model += Y11 <= 2400*(X11 + X13)	# maximum megawatts from #1 from 6–2
model += Y12 <= 2400*(X12 + X13)	# maximum megawatts from #1 from 2–10
model += Y21 <= 2100*(X21 + X23)	# maximum megawatts from #2 from 6–2
model += Y22 <= 2100*(X22 + X23)	# maximum megawatts from #2 from 2–10
model += Y31 <= 3300*(X31 + X33)	# maximum megawatts from #3 from 6–2
model += Y32 <= 3300*(X32 + X33)	# maximum megawatts from #3 from 2–10
model += X11 + X12 + X13 <= 1	    # generator #1 starts up at most once
model += X21 + X22 + X23 <= 1	    # generator #2 starts up at most once
model += X31 + X32 + X33 <= 1	    # generator #3 starts up at most once

# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print(f'Generators on/off = {X11.varValue:.0f},{X12.varValue:.0f},{X13.varValue:.0f},{X21.varValue:.0f},\
{X22.varValue:.0f},{X23.varValue:.0f},{X31.varValue:.0f},{X32.varValue:.0f},{X33.varValue:.0f}')

print(f'Megawatts generated = {Y11.varValue},{Y12.varValue},{Y21.varValue},\
{Y22.varValue},{Y31.varValue},{Y32.varValue}')

print(f'Total Cost is = ${pulp.value(model.objective)}')
