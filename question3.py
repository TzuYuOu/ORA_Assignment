from pulp import *
import math

# constant
# p_i = [16,16,16,16,9,9,9,9,9,18,18,18]
p_i = [33,30,25,18,18]
# q_i = [8,8,8,8,9,9,9,9,9,3,3,3]
q_i = [10,11,15,14,10]
X_LOWER_BOUND = 10
Y_LOWER_BOUND = 10
# X_UPPER_BOUND = 163
# Y_UPPER_BOUND = 163
X_UPPER_BOUND = 124
Y_UPPER_BOUND = 124

m = 10
A = [0]*(m+1)
A[1] = X_LOWER_BOUND
A[-1] = X_UPPER_BOUND
a_slice = (X_UPPER_BOUND-X_LOWER_BOUND)/(m-1) 
for i in range(2,m):
    A[i] = A[i-1]+a_slice

sj = [0]*m
for j in range(1,m):
    sj[j] = (math.log(A[j+1])-math.log(A[j])) / (A[j+1]-A[j])

# Define decision variables
x = LpVariable("x",X_LOWER_BOUND,X_UPPER_BOUND,cat='Continuous')
y = LpVariable("y",Y_LOWER_BOUND,Y_UPPER_BOUND,cat='Continuous')

x_i = {}
y_i = {}
s_i = {}
for i in range(1,len(p_i)+1):
    x_i["x_{}".format(i)] = LpVariable("x_{}".format(i),0,None,cat='Continuous')
    y_i["y_{}".format(i)] = LpVariable("y_{}".format(i),0,None,cat='Continuous')
    s_i["s_{}".format(i)] = LpVariable("s_{}".format(i),0,1,LpInteger)

u_ik = {}
v_ik = {}
for i in range(1,len(p_i)+1):
    for k in range(i+1,len(p_i)+1):
        u_ik["u_{}_{}".format(i,k)] = LpVariable("u_{}_{}".format(i,k),0,1,LpInteger)
        v_ik["v_{}_{}".format(i,k)] = LpVariable("v_{}_{}".format(i,k),0,1,LpInteger)

uj = {}
wj = {}
for j in range(1,m+1):
    uj["u_{}".format(j)] = LpVariable("u_{}".format(j),0,1,LpInteger)
    wj["w_{}".format(j)] = LpVariable("w_{}".format(j),0,None,cat='Continuous')

yuj = {}
ywj = {}
for j in range(1,m+1):
    yuj["yu_{}".format(j)] = LpVariable("yu_{}".format(j),0,1,LpInteger)
    ywj["yw_{}".format(j)] = LpVariable("yw_{}".format(j),0,None,cat='Continuous')
# Define problem
prob =  LpProblem("MinimizeRectangleArea",LpMinimize)
prob += math.log(A[1]) + sj[1]*(x-A[1]) + lpSum([ (sj[j]-sj[j-1])*(A[j]*uj["u_{}".format(j)]+x-A[j]-wj["w_{}".format(j)]) for j in range(2,m)])\
        + math.log(A[1]) + sj[1]*(y-A[1]) + lpSum([ (sj[j]-sj[j-1])*(A[j]*yuj["yu_{}".format(j)]+y-A[j]-ywj["yw_{}".format(j)]) for j in range(2,m)])  , "Area"
# constraint 2,3
for i in range(1,len(p_i)+1):
    for k in range(i+1,len(p_i)+1):
        prob += (x_i["x_{}".format(i)]-x_i["x_{}".format(k)]) + u_ik["u_{}_{}".format(i,k)]*X_UPPER_BOUND + v_ik["v_{}_{}".format(i,k)]*X_UPPER_BOUND\
                >= 0.5*(p_i[i-1]*s_i["s_{}".format(i)] + q_i[i-1]*(1-s_i["s_{}".format(i)]) + p_i[k-1]*s_i["s_{}".format(k)] + q_i[k-1]*(1-s_i["s_{}".format(k)]))
        prob += (x_i["x_{}".format(k)]-x_i["x_{}".format(i)]) + (1-u_ik["u_{}_{}".format(i,k)])*X_UPPER_BOUND + v_ik["v_{}_{}".format(i,k)]*X_UPPER_BOUND\
                >= 0.5*(p_i[i-1]*s_i["s_{}".format(i)] + q_i[i-1]*(1-s_i["s_{}".format(i)]) + p_i[k-1]*s_i["s_{}".format(k)] + q_i[k-1]*(1-s_i["s_{}".format(k)]))
# constraint 4,5
for i in range(1,len(p_i)+1):
    for k in range(i+1,len(p_i)+1):
        prob += (y_i["y_{}".format(i)]-y_i["y_{}".format(k)]) + u_ik["u_{}_{}".format(i,k)]*Y_UPPER_BOUND + (1-v_ik["v_{}_{}".format(i,k)])*Y_UPPER_BOUND\
                >= 0.5*(p_i[i-1]*(1-s_i["s_{}".format(i)]) + q_i[i-1]*s_i["s_{}".format(i)] + p_i[k-1]*(1-s_i["s_{}".format(k)]) + q_i[k-1]*s_i["s_{}".format(k)])
        prob += (y_i["y_{}".format(k)]-y_i["y_{}".format(i)]) + (1-u_ik["u_{}_{}".format(i,k)])*Y_UPPER_BOUND + (1-v_ik["v_{}_{}".format(i,k)])*Y_UPPER_BOUND\
                >= 0.5*(p_i[i-1]*(1-s_i["s_{}".format(i)]) + q_i[i-1]*s_i["s_{}".format(i)] + p_i[k-1]*(1-s_i["s_{}".format(k)]) + q_i[k-1]*s_i["s_{}".format(k)])
# constraint 6
prob += X_UPPER_BOUND >= x
for i in range(1,len(p_i)+1):
    prob += x >= x_i["x_{}".format(i)] + (p_i[i-1]*s_i["s_{}".format(i)] + q_i[i-1]*(1-s_i["s_{}".format(i)]))/2
# constraint 7
prob += Y_UPPER_BOUND >= y
for i in range(1,len(p_i)+1):
    prob += y >= y_i["y_{}".format(i)] + (p_i[i-1]*(1-s_i["s_{}".format(i)]) + q_i[i-1]*s_i["s_{}".format(i)])/2
# constraint 8,9
for i in range(1,len(p_i)+1):
    prob += x_i["x_{}".format(i)] - (p_i[i-1]*s_i["s_{}".format(i)] + q_i[i-1]*(1-s_i["s_{}".format(i)]))/2 >= 0
    prob += y_i["y_{}".format(i)] - (p_i[i-1]*(1-s_i["s_{}".format(i)]) + q_i[i-1]*s_i["s_{}".format(i)])/2 >= 0

# ln x constraint
# constraint i
for j in range(2,m+1):
    prob += -A[m]*uj["u_{}".format(j)] <= x - A[j]
    prob += x - A[j] <= A[m]*(1-uj["u_{}".format(j)])
# constraint ii
for j in range(2,m+1):
    prob += -A[m]*uj["u_{}".format(j)] <= wj["w_{}".format(j)]
    prob += wj["w_{}".format(j)] <= A[m]*uj["u_{}".format(j)]
# constraint iii
for j in range(2,m+1):
    prob += A[m]*(uj["u_{}".format(j)]-1) + x <= wj["w_{}".format(j)]
    prob += wj["w_{}".format(j)] <= A[m]*(1-uj["u_{}".format(j)]) + x
# constraint iv
for j in range(2,m+1):
    uj["u_{}".format(j)] >= uj["u_{}".format(j-1)]

# ln y constraint
# constraint i
for j in range(2,m+1):
    prob += -A[m]*yuj["yu_{}".format(j)] <= y - A[j]
    prob += y - A[j] <= A[m]*(1-yuj["yu_{}".format(j)])
# constraint ii
for j in range(2,m+1):
    prob += -A[m]*yuj["yu_{}".format(j)] <= ywj["yw_{}".format(j)]
    prob += ywj["yw_{}".format(j)] <= A[m]*yuj["yu_{}".format(j)]
# constraint iii
for j in range(2,m+1):
    prob += A[m]*(yuj["yu_{}".format(j)]-1) + y <= ywj["yw_{}".format(j)]
    prob += ywj["yw_{}".format(j)] <= A[m]*(1-yuj["yu_{}".format(j)]) + x
# constraint iv
for j in range(2,m+1):
    yuj["yu_{}".format(j)] >= yuj["yu_{}".format(j-1)]

prob.writeLP("MinimizeRectangleArea.lp")
prob.solve()
print("Status:", LpStatus[prob.status])
print("Objective function value = ", value(prob.objective))
print("x: {}".format(x.varValue))
print("y: {}".format(y.varValue))
print("Rectangle Area: {}".format(x.varValue*y.varValue))
