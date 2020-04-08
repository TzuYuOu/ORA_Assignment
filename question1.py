from pulp import *

# Define input data
# Material cost of material p1,p2,p3 supplied by supplier v1,v2 at time t1~t5
Mcost = [10.5,6.5,8.5,20.5,7.5,7.5, 10.4,6.4,8.4,20.4,7.4,7.4, 10.3,6.3,8.3,20.3,7.3,7.3, 10.2,6.2,8.2,20.2,7.2,7.2, 10.1,6.1,8.1,20.1,7.1,7.1]
# Production cost of goods g1 producted by facilities f1,f2 at time t1~t5
Pcost =[0.4,0.45]*5
# Transportation cost of material p1,p2,p3 from supplier v1,v2 to facilities f1,f2 at time t1~t5
VF_Tcost =[0.01]*60
# Transportation cost of goods g1 from facilities f1,f2 to warehouse w1,w2 at time t1~t5
FW_Tcost = [0.2,0.3,0.5,0.1]*5
# Transportation cost of goods g1 from w1,w2 to c1,c2,c3 at time t1~t5 
WC_Tcost = [0.6,0.4,0.3,0.3,0.5,0.4]*5
# Inventory cost of material p1~p3 in facilities f1,f2 at time t1~t5
FM_Icost = [0.02, 0.02, 0.02, 0.01, 0.01, 0.01]*5
# Inventory cost of goods g1 in facilities f1,f2 at time t1~t5
FG_Icost = [0.1,0.09]*5
# Inventory cost of goods g1 in warehouse w1,w2 at time t1~t5
W_Icost = [0.07,0.05]*5
# Amount of material p1~p3 needed for producing goods g1
BOM = [1,2,3]
# Transportation lead time from suppliers v1,v2 to facilities f1,f2 
Tvf = [[1,1],[1,1]]
# Transportation lead time from facilities f1,f2 to warehouse w1,w2
Tfw = [[1,1],[1,1]]
# Transportation lead time from warehouse w1,w2 to customer c1~c3
Twc = [[1,1,1],[1,1,1]]
# Production time of finish goods g1 in facilities f1,f2
Tbomfg = [1,1]
# Demand of goods g by customer c1~c3 at time t1~t5
LCtcg = {    
    'LC_t1_c1_g1': 0,
    'LC_t1_c2_g1': 0,
    'LC_t1_c3_g1': 0,
    'LC_t2_c1_g1': 0,
    'LC_t2_c2_g1': 0,
    'LC_t2_c3_g1': 0,
    'LC_t3_c1_g1': 0,
    'LC_t3_c2_g1': 0,
    'LC_t3_c3_g1': 0,
    'LC_t4_c1_g1': 30,
    'LC_t4_c2_g1': 20,
    'LC_t4_c3_g1': 10,
    'LC_t5_c1_g1': 55,
    'LC_t5_c2_g1': 40,
    'LC_t5_c3_g1': 50,

}

# Define decision variables
# Amount of p1~p3 purchased from v1,v2 at t1~t5
LV = {}
for t in range(1,6):
    for v in range(1,3):
        for p in range(1,4):
            LV["LV_t{}_t{}{}".format(t,v,p)] = LpVariable("LV_t{}_t{}{}".format(t,v,p),0,500,LpInteger)

# Amount of p1~p3 transported from v1,v2 to f1,f2 at t1~t5
Rtvfp = {}
for t in range(1,6):
    for v in range(1,3):
        for f in range(1,3):
            for p in range(1,4):
                Rtvfp["R_t{}_v{}_f{}_p{}".format(t,v,f,p)] = LpVariable("R_t{}_v{}_f{}_p{}".format(t,v,f,p),0,None,LpInteger)

# Amount of goods g1 which f1,f2 producted at t1~t5
Rtfg = {}
for t in range(1,6):
    for f in range(1,3):
        if f == 1:
            Rtfg["R_t{}_f{}_g1".format(t,f)] = LpVariable("R_t{}_f{}_g1".format(t,f),0,70,LpInteger)
        else:
            Rtfg["R_t{}_f{}_g1".format(t,f)] = LpVariable("R_t{}_f{}_g1".format(t,f),0,35,LpInteger)
# Inventory of p1~p3 in f1,f2 at t1~t5
LFtfp = {}
for t in range(1,6):
    for f in range(1,3):
        for p in range(1,4):
            LFtfp["LF_t{}_f{}_p{}".format(t,f,p)] = LpVariable("LF_t{}_f{}_p{}".format(t,f,p),0,None,LpInteger)



# Inventory of g1 in f1,f2 at t1~t5
LFtfg = {}
for t in range(1,6):
    for f in range(1,3):
        LFtfg["LF_t{}_f{}_g1".format(t,f)] = LpVariable("LF_t{}_f{}_g1".format(t,f),0,None,LpInteger)
# Inventory of g1 in w1,w2 at t1~t5
LWtwg = {} 
for t in range(1,6):
    for w in range(1,3):
        if w == 1:
            LWtwg["LW_t{}_w{}_g1".format(t,w)] = LpVariable("LW_t{}_w{}_g1".format(t,w),0,400,LpInteger)
        else:
            LWtwg["LW_t{}_w{}_g1".format(t,w)] = LpVariable("LW_t{}_w{}_g1".format(t,w),0,500,LpInteger)
# Amounts of g1 transported from f1,f2 to w1,w2 at t1~t5
Rtfwg = {}
for t in range(1,6):
    for f in range(1,3):
        for w in range(1,3):
            Rtfwg["R_t{}_f{}_w{}_g1".format(t,f,w)] = LpVariable("R_t{}_f{}_w{}_g1".format(t,f,w),0,None,LpInteger)
# Amounts of g1 transported from w1,w2 to c1,c2,c3 at t1~t5
Rtwcg = {}
for t in range(1,6):
    for w in range(1,3):
        for c in range(1,4):
            Rtwcg["R_t{}_w{}_c{}_g1".format(t,w,c)] = LpVariable("R_t{}_w{}_c{}_g1".format(t,w,c),0,None,LpInteger)

# Define problem
prob =  LpProblem("SCM",LpMinimize)
# Set objective function
prob += lpSum([ v1 * v2 for v1 ,(_,v2) in zip(Mcost, LV.items())]) +lpSum([ v1 * v2 for v1 ,(_,v2) in zip(VF_Tcost, Rtvfp.items())])\
        +lpSum([ v1 * v2 for v1 ,(_,v2) in zip(Pcost, Rtfg.items())]) +lpSum([ v1 * v2 for v1 ,(_,v2) in zip(FM_Icost, LFtfp.items())])\
        +lpSum([ v1 * v2 for v1 ,(_,v2) in zip(FG_Icost, LFtfg.items())]) +lpSum([ v1 * v2 for v1 ,(_,v2) in zip(W_Icost, LWtwg.items())])\
        +lpSum([ v1 * v2 for v1 ,(_,v2) in zip(FW_Tcost, Rtfwg.items())]) +lpSum([ v1 * v2 for v1 ,(_,v2) in zip(WC_Tcost, Rtwcg.items())]), "Total cost"
# Flow constraints
f_constraint_nums = 1
for t in range(1,6):
    for v in range(1,3):
        for p in range(1,4):
            prob += LV["LV_t{}_t{}{}".format(t,v,p)] == Rtvfp["R_t{}_v{}_f1_p{}".format(t,v,p)]+Rtvfp["R_t{}_v{}_f2_p{}".format(t,v,p)], "Constraint{}".format(f_constraint_nums)
            f_constraint_nums += 1

for t in range(1,5):
    for f in range(1,3):
        for p in range(1,4):
            if t == 1:
                prob += LFtfp["LF_t{}_f{}_p{}".format(t,f,p)] - BOM[p-1]*Rtfg["R_t{}_f{}_g1".format(t,f)] == LFtfp["LF_t{}_f{}_p{}".format(t+1,f,p)], "Constraint{}".format(f_constraint_nums)
            else:
                prob += LFtfp["LF_t{}_f{}_p{}".format(t,f,p)] + Rtvfp["R_t{}_v1_f{}_p{}".format(t-1,f,p)] + Rtvfp["R_t{}_v2_f{}_p{}".format(t-1,f,p)] - BOM[p-1]*Rtfg["R_t{}_f{}_g1".format(t,f)] == LFtfp["LF_t{}_f{}_p{}".format(t+1,f,p)], "Constraint{}".format(f_constraint_nums)
            f_constraint_nums +=1

for t in range(1,5):
    for f in range(1,3):
        if t == 1:
            prob += LFtfg["LF_t{}_f{}_g1".format(t,f)] - Rtfwg["R_t{}_f{}_w1_g1".format(t,f)] - Rtfwg["R_t{}_f{}_w2_g1".format(t,f)] == LFtfg["LF_t{}_f{}_g1".format(t+1,f)], "Constraint{}".format(f_constraint_nums)
        else:
            prob += LFtfg["LF_t{}_f{}_g1".format(t,f)] + Rtfg["R_t{}_f{}_g1".format(t-1,f)] - Rtfwg["R_t{}_f{}_w1_g1".format(t,f)] - Rtfwg["R_t{}_f{}_w2_g1".format(t,f)] == LFtfg["LF_t{}_f{}_g1".format(t+1,f)], "Constraint{}".format(f_constraint_nums)
        f_constraint_nums += 1

for t in range(1,5):
    for w in range(1,3):
        if t==1:
            prob += LWtwg["LW_t{}_w{}_g1".format(t,w)] - Rtwcg["R_t{}_w{}_c1_g1".format(t,w)] - Rtwcg["R_t{}_w{}_c2_g1".format(t,w)] - Rtwcg["R_t{}_w{}_c3_g1".format(t,w)] == LWtwg["LW_t{}_w{}_g1".format(t+1,w)], "Constraint{}".format(f_constraint_nums)
        else:
            prob += LWtwg["LW_t{}_w{}_g1".format(t,w)] + Rtfwg["R_t{}_f1_w{}_g1".format(t-1,w)] + Rtfwg["R_t{}_f2_w{}_g1".format(t-1,w)] - Rtwcg["R_t{}_w{}_c1_g1".format(t,w)] - Rtwcg["R_t{}_w{}_c2_g1".format(t,w)] - Rtwcg["R_t{}_w{}_c3_g1".format(t,w)] == LWtwg["LW_t{}_w{}_g1".format(t+1,w)], "Constraint{}".format(f_constraint_nums)
        f_constraint_nums += 1

for t in range(2,6):
    for c in range(1,4):
        prob += Rtwcg["R_t{}_w1_c{}_g1".format(t-1,c)] + Rtwcg["R_t{}_w2_c{}_g1".format(t-1,c)]  == LCtcg["LC_t{}_c{}_g1".format(t,c)], "Constraints{}".format(f_constraint_nums)
        f_constraint_nums += 1 


prob += LFtfp["LF_t1_f1_p1"] == 200, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1
prob += LFtfp["LF_t1_f1_p2"] == 300, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1
prob += LFtfp["LF_t1_f1_p3"] == 300, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1
prob += LFtfp["LF_t1_f2_p1"] == 100, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1
prob += LFtfp["LF_t1_f2_p2"] == 100, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1
prob += LFtfp["LF_t1_f2_p3"] == 100, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1

prob += LFtfg["LF_t1_f1_g1"] == 0, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1
prob += LFtfg["LF_t1_f2_g1"] == 0, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1

prob += LWtwg["LW_t1_w1_g1"] == 0, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1
prob += LWtwg["LW_t1_w2_g1"] == 0, "Constraint{}".format(f_constraint_nums)
f_constraint_nums += 1

prob.writeLP("SupplyChainModel.lp")
prob.solve()
print("Status:", LpStatus[prob.status])
print("Total Cost = ", value(prob.objective))


# for v in prob.variables():
#     print(v.name, "=", v.varValue)
# print(prob)