#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:18:32 2020

@author: tzuyuou
"""

from pulp import *



# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Nutrition Problem",LpMinimize)

# The 6 variables are created with a lower limit of zero and integar type
x1=LpVariable("Bread",0,None,LpInteger)
x2=LpVariable("Peanut butter",0,None,LpInteger)
x3=LpVariable("Strawberry jelly",0,None,LpInteger)
x4=LpVariable("Graham cracker",0,None,LpInteger)
x5=LpVariable("Milk",0,None,LpInteger)
x6=LpVariable("Juice",0,None,LpInteger)
# The objective function is added to 'prob' first
prob += 5*x1 + 4*x2 + 7*x3 + 8*x4 + 15*x5 + 35*x6, "Total Cost of Ingredients per meal"

# The seven constraints are entered
prob += 400 <= 70*x1+100*x2+50*x3+60*x4+150*x5+100*x6 <= 600, "Total Calories",
prob += 10*x1+75*x2+20*x4+70*x5 <= 21*x1+30*x2+15*x3+18*x4+45*x5+30*x6, "FatRequirement"
prob += 3*x3+2*x5+120*x6 >= 60, "VltaminCRequirement"
prob += 3*x1+4*x2+x4+8*x5+x6 >= 12, "ProtienRequirement"
prob += x1 == 2, "SandwichRequirement"
prob += x2 >= 2*x3, "ButterRequirement"
prob += x5+x6 >= 1, "LiquidRequirement"

# The problem data is written to an .lp file
prob.writeLP("NutritionModel.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
#print ("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print( v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print ("Total Cost of Ingredients per meal = ", value(prob.objective))

