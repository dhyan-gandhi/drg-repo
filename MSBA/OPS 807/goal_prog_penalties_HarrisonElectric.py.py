# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 21:52:08 2018
 problem statement
Company produces two products, old-fashioned chandeliers and ceiling fans
Both require a two-step production process involving wiring and assembly
It takes about 2 hours to wire each chandelier and 3 hours to wire a ceiling fan
Final assembly of the chandeliers and fans requires 6 and 5 hours, respectively
Only 12 hours of wiring time and 30 hours of assembly time are available
Each chandelier produced nets the firm $7 and each fan $6

Achieve several goals that are equal in priority
Goal 1: to produce a profit of $30 if possible during the production period
Goal 2: to fully utilize the available wiring department hours
Goal 3: to avoid overtime in the assembly department
Goal 4: to meet a contract requirement to produce at least seven ceiling fans

The deviational variables can be defined as
	d1– = underachievement of the profit target
	d1+ = overachievement of the profit target
	d2– = idle time in the wiring department (underutilization)
	d2+ = overtime in the wiring department (overutilization)
	d3– = idle time in the assembly department (underutilization)
	d3+ = overtime in the assembly department (overutilization)
	d4– = underachievement of the ceiling fan goal
	d4+ = overachievement of the ceiling fan goal

Management is unconcerned about d1+, d2+, d3–, and d4+ so these may be omitted from the objective function

Here we assume priorities and weights to penalize deviation from the target values
We consider p1 = p2 = p3 = p4 = p5 = 1, same level of priority for all
w1 = w2 = w3 = w5 = 1, all penalty weights are the same and equal 1 except w4 which is twice as important as the rest of the weights
w4 = 2 * w1 
Suppose Harrison decides to add another goal of producing at least two chandeliers
The goal of producing seven ceiling fans is considered twice as important as this goal
The goal of two chandeliers is assigned a weight of 1 and the goal of seven ceiling fans is assigned a weight of 2 and both of these will be priority level 4
The new constraint and objective function are
    
    
	Minimize	total 	= P1d1– + P2d2– + P3d3+ + P4(2d4–) + P4d5–
	deviation

Minimize total deviation  =  d1– + d2– + d3+ + d4–

subject to
 	 $7X1 +	$6X2	+ d1– – d1+	=	$30	(profit constraint)
	  2X1 +	  3X2	+ d2– – d2+	=	12	(wiring hours constraint)
	  6X1 +	  5X2	+ d3– – d3+	=	30	(assembly hours constraint)
	            	X2	+ d4– – d4+	=	7	(ceiling fan constraint)
                   X1 + d5– – d5+ = 2  (chandeliers)                  
		All Xi, di variables		≥	0


where
		X1 = number of chandeliers produced 
		X2 = number of ceiling fans produced
        
@author: jahan
        
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
d2_neg = pulp.LpVariable("d2_neg", lowBound=0, cat='Integer')
d2_plus = pulp.LpVariable("d2_plus", lowBound=0, cat='Integer')
d3_neg = pulp.LpVariable("d3_neg", lowBound=0, cat='Integer')
d3_plus = pulp.LpVariable("d3_plus", lowBound=0, cat='Integer')
d4_neg = pulp.LpVariable("d4_neg", lowBound=0, cat='Integer')
d4_plus = pulp.LpVariable("d4_plus", lowBound=0, cat='Integer')
d5_neg = pulp.LpVariable("d5_neg", lowBound=0, cat='Integer')
d5_plus = pulp.LpVariable("d5_plus", lowBound=0, cat='Integer')

# assume all priorities are at the same level, all goals are qually improtant
# and the difference is only in weights
# objective function = P1d1– + P2d2– + P3d3+ + P4(2d4–) + P4d5–
p1 = p2 = p3 = p4 = p5 = 1
w1 = w2 = w3 = w5 = 1
#w4 = 2 * w1
w4 = w5 = 10 * w1

# Objective function
model += p1 * w1 * d1_neg + p2 * w2* d2_neg + p3 * w3 * d3_plus + p4 * w4 * d4_neg + p5 * w5* d5_neg, "under_over"

# Constraints
model += 7 * x1 + 6 * x2 + d1_neg - d1_plus == 30
model += 2 * x1 + 3 * x2 + d2_neg - d2_plus == 12
model += 6 * x1 + 5 * x2 + d3_neg - d3_plus == 30
model += x2 + d4_neg - d4_plus == 7
model += x1 + d5_neg - d5_plus == 2



# Solve our problem
model.solve()
pulp.LpStatus[model.status]


# Print our decision variable values
print( "Number of chandeliers produced = {}".format(x1.varValue))
print( "Number of ceiling fans produced = {}".format(x2.varValue)) 
print( "Underachievement of Target Profit = {}".format(d1_neg.varValue))
print( "Idle time of wiring  = {}".format(d2_neg.varValue)) 
print( "Overtime in the assembly  = {}".format(d3_plus.varValue))
print( "Underachievement of Target ceiling fan = {}".format(d4_neg.varValue)) 
print( "Underachievement of Target chandelier = {}".format(d5_neg.varValue)) 