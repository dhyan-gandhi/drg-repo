# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:18:49 2019

@author: jg
"""

"""

8-18.	

    X1	= number of medical patients
	X2	= number of surgical patients

Maximize revenue = $2,280X1 + $1,515X2

subject to

	8X1 +  5X2	  <= 32,850 (patient-days available = 365 days  90 new beds)
    3.1X1 + 2.6X2 <= 15,000 (lab tests)
	1X1 +   2X2	  <= 7,000 (x-rays)
	X2	          <= 2,800 (operations/surgeries)
	X1, X2	>= 0

solution:
    
	X1	= 2,791 medical patients
	X2	= 2,105 surgical patients
	revenue	= $9,551,659 per year 
To convert X1 and X2 to number of medical versus surgical beds, find the total number of hospital days for each type of patient:
	medical	= (2,791 patients)(8 days/patient)
		= 22,328 days
	surgical	= (2,105 patients)(5 days/patient)
		= 10,525 days
	total	= 32,853 days (The rounding causes this to be slightly higher than the limit.)
This represents 68% medical days and 32% surgical days, which yields 61 medical beds and 29 surgical beds.


"""

import pulp 


model = pulp.LpProblem("maximizing problem", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')


# Objective function
model += 2280 * x1 + 1515.0 * x2, "maximize"


# Constraints     
model += 8 * x1 + 5 * x2 <= 32850 
model += 3.1 * x1 + 2.6 * x2 <= 15000 #(lab tests) 
model += x1 + 2 * x2 <= 7000          #(x-rays)
model += x2 <= 2800                   # (operations/surgeries)


# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( f'Number of medical patients = {x1.varValue}')
print( f'Number of surgical patients = {x2.varValue}') 
print(f'Total revenue is = ${pulp.value(model.objective)}')
print(f'Total number of days beds are needed: {x1.varValue * 8 + x2.varValue * 5}')
