from pulp import *
'''
W = ([5,3,0,0],[0,1,8,4])
V = ([0,6],[6,0])
a = ([0,4,6,10])
b = ([2,0,8,4])
'''
# define constant
V = 6
W = [[5,3,0,0],[0,1,8,4]]
A = [0,4,6,10]
B = [2,0,8,4]


# define decision variable
x_j = LpVariable("x_j",0,None,LpInteger)
x_k = LpVariable("x_k",0,None,LpInteger)
y_j = LpVariable("y_j",0,None,LpInteger)
y_k = LpVariable("y_k",0,None,LpInteger)

p_jk = LpVariable("p_jk",0,None,LpInteger)
q_jk = LpVariable("q_jk",0,None,LpInteger)

yp_jk = LpVariable("yp_jk",0,None,LpInteger)
yq_jk = LpVariable("yq_jk",0,None,LpInteger)

r_j1 = LpVariable("r_j1",0,None,LpInteger)
r_j2 = LpVariable("r_j2",0,None,LpInteger)
r_j3 = LpVariable("r_j3",0,None,LpInteger)
r_j4 = LpVariable("r_j4",0,None,LpInteger)

s_j1 = LpVariable("s_j1",0,None,LpInteger)
s_j2 = LpVariable("s_j2",0,None,LpInteger)
s_j3 = LpVariable("s_j3",0,None,LpInteger)
s_j4 = LpVariable("s_j4",0,None,LpInteger)

r_k1 = LpVariable("r_k1",0,None,LpInteger)
r_k2 = LpVariable("r_k2",0,None,LpInteger)
r_k3 = LpVariable("r_k3",0,None,LpInteger)
r_k4 = LpVariable("r_k4",0,None,LpInteger)

s_k1 = LpVariable("s_k1",0,None,LpInteger)
s_k2 = LpVariable("s_k2",0,None,LpInteger)
s_k3 = LpVariable("s_k3",0,None,LpInteger)
s_k4 = LpVariable("s_k4",0,None,LpInteger)

yr_j1 = LpVariable("yr_j1",0,None,LpInteger)
yr_j2 = LpVariable("yr_j2",0,None,LpInteger)
yr_j3 = LpVariable("yr_j3",0,None,LpInteger)
yr_j4 = LpVariable("yr_j4",0,None,LpInteger)

ys_j1 = LpVariable("ys_j1",0,None,LpInteger)
ys_j2 = LpVariable("ys_j2",0,None,LpInteger)
ys_j3 = LpVariable("ys_j3",0,None,LpInteger)
ys_j4 = LpVariable("ys_j4",0,None,LpInteger)

yr_k1 = LpVariable("yr_k1",0,None,LpInteger)
yr_k2 = LpVariable("yr_k2",0,None,LpInteger)
yr_k3 = LpVariable("yr_k3",0,None,LpInteger)
yr_k4 = LpVariable("yr_k4",0,None,LpInteger)

ys_k1 = LpVariable("ys_k1",0,None,LpInteger)
ys_k2 = LpVariable("ys_k2",0,None,LpInteger)
ys_k3 = LpVariable("ys_k3",0,None,LpInteger)
ys_k4 = LpVariable("ys_k4",0,None,LpInteger)

# define problem
prob =  LpProblem("Facility planing",LpMinimize)
# define objective function
prob += V*(p_jk+q_jk) + V*(yp_jk+yq_jk) + W[0][0]*(r_j1+s_j1) + W[0][1]*(r_j2+s_j2) + W[0][2]*(r_j3+s_j3) + W[0][3]*(r_j4+s_j4)\
        + W[1][0]*(r_k1+s_k1) + W[1][1]*(r_k2+s_k2) + W[1][2]*(r_k3+s_k3) + W[1][3]*(r_k4+s_k4)\
        + W[0][0]*(yr_j1+ys_j1) + W[0][1]*(yr_j2+ys_j2) + W[0][2]*(yr_j3+ys_j3) + W[0][3]*(yr_j4+ys_j4)\
        + W[1][0]*(yr_k1+ys_k1) + W[1][1]*(yr_k2+ys_k2) + W[1][2]*(yr_k3+ys_k3) + W[1][3]*(yr_k4+ys_k4) ,"Total Cost"
# add constraints
prob += x_j-q_jk+p_jk == x_k, "Two new facility x constraint"
prob += y_j-yq_jk+yp_jk == y_k, "Two new facility y constraint"

prob += x_j-r_j1+s_j1 == A[0], "constraint1"
prob += x_j-r_j2+s_j2 == A[1], "constraint2"
prob += x_j-r_j3+s_j3 == A[2], "constraint3"
prob += x_j-r_j4+s_j4 == A[3], "constraint4"

prob += x_k-r_k1+s_k1 == A[0], "constraint5"
prob += x_k-r_k2+s_k2 == A[1], "constraint6"
prob += x_k-r_k3+s_k3 == A[2], "constraint7"
prob += x_k-r_k4+s_k4 == A[3], "constraint8"

prob += y_j-yr_j1+ys_j1 == B[0], "constraint9"
prob += y_j-yr_j2+ys_j2 == B[1], "constraint10"
prob += y_j-yr_j3+ys_j3 == B[2], "constraint11"
prob += y_j-yr_j4+ys_j4 == B[3], "constraint12"

prob += y_k-yr_k1+ys_k1 == B[0], "constraint13"
prob += y_k-yr_k2+ys_k2 == B[1], "constraint14"
prob += y_k-yr_k3+ys_k3 == B[2], "constraint15"
prob += y_k-yr_k4+ys_k4 == B[3], "constraint16"

prob.writeLP("FacilityPlanModel.lp")
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])


print("New Facility 1 (x,y) = ({},{})".format(x_j.varValue, y_j.varValue))
print("New Facility 2 (x,y) = ({},{})".format(x_k.varValue, y_k.varValue))    

# The optimised objective function value is printed to the screen
print("Total Cost = ", value(prob.objective))

# if __name__  == "__main__":
#     print(W[0][1])