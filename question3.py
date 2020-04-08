from pulp import *
import math

p_i = [16,16,16,16,9,9,9,9,9,18,18,18]
q_i = [8,8,8,8,9,9,9,9,9,3,3,3]

# Define decision variables
x_i = {}
y_i = {}
s_i = {}
for i in range(1,13):
    x_i["x_{}".format(i)] = LpVariable("x_{}".format(i),0,None,LpInteger)
    y_i["y_{}".format(i)] = LpVariable("y_{}".format(i),0,None,LpInteger)
    s_i["s_{}".format(i)] = LpVariable("s_{}".format(i),0,1,LpInteger)

x = LpVariable("x",0,None,LpInteger)
y = LpVariable("y",0,None,LpInteger)

# Define problem
prob =  LpProblem("MinimizeRectangleArea",LpMinimize)
prob += x+y , "Area"

# constraint 8,9
for i in range(1,13):
    prob += x_i["x_{}".format(i)] - (p_i[i-1]*s_i["s_{}".format(i)] + q_i[i-1](1-s_i["s_{}".format(i)]))/2 >= 0
    prob += y_i["y_{}".format(i)] - (p_i[i-1]*(1-s_i["s_{}".format(i)]) + q_i[i-1]*s_i["s_{}".format(i)])/2 >= 0