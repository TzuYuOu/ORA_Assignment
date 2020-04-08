\* Facility planing *\
Minimize
Total_Cost: 6 p_jk + 6 q_jk + 5 r_j1 + 3 r_j2 + r_k2 + 8 r_k3 + 4 r_k4
 + 5 s_j1 + 3 s_j2 + s_k2 + 8 s_k3 + 4 s_k4 + 6 yp_jk + 6 yq_jk + 5 yr_j1
 + 3 yr_j2 + yr_k2 + 8 yr_k3 + 4 yr_k4 + 5 ys_j1 + 3 ys_j2 + ys_k2 + 8 ys_k3
 + 4 ys_k4
Subject To
Two_new_facility_x_constraint: p_jk - q_jk + x_j - x_k = 0
Two_new_facility_y_constraint: y_j - y_k + yp_jk - yq_jk = 0
constraint1: - r_j1 + s_j1 + x_j = 0
constraint10: y_j - yr_j2 + ys_j2 = 0
constraint11: y_j - yr_j3 + ys_j3 = 8
constraint12: y_j - yr_j4 + ys_j4 = 4
constraint13: y_k - yr_k1 + ys_k1 = 2
constraint14: y_k - yr_k2 + ys_k2 = 0
constraint15: y_k - yr_k3 + ys_k3 = 8
constraint16: y_k - yr_k4 + ys_k4 = 4
constraint2: - r_j2 + s_j2 + x_j = 4
constraint3: - r_j3 + s_j3 + x_j = 6
constraint4: - r_j4 + s_j4 + x_j = 10
constraint5: - r_k1 + s_k1 + x_k = 0
constraint6: - r_k2 + s_k2 + x_k = 4
constraint7: - r_k3 + s_k3 + x_k = 6
constraint8: - r_k4 + s_k4 + x_k = 10
constraint9: y_j - yr_j1 + ys_j1 = 2
Bounds
0 <= p_jk
0 <= q_jk
0 <= r_j1
0 <= r_j2
0 <= r_j3
0 <= r_j4
0 <= r_k1
0 <= r_k2
0 <= r_k3
0 <= r_k4
0 <= s_j1
0 <= s_j2
0 <= s_j3
0 <= s_j4
0 <= s_k1
0 <= s_k2
0 <= s_k3
0 <= s_k4
0 <= x_j
0 <= x_k
0 <= y_j
0 <= y_k
0 <= yp_jk
0 <= yq_jk
0 <= yr_j1
0 <= yr_j2
0 <= yr_j3
0 <= yr_j4
0 <= yr_k1
0 <= yr_k2
0 <= yr_k3
0 <= yr_k4
0 <= ys_j1
0 <= ys_j2
0 <= ys_j3
0 <= ys_j4
0 <= ys_k1
0 <= ys_k2
0 <= ys_k3
0 <= ys_k4
Generals
p_jk
q_jk
r_j1
r_j2
r_j3
r_j4
r_k1
r_k2
r_k3
r_k4
s_j1
s_j2
s_j3
s_j4
s_k1
s_k2
s_k3
s_k4
x_j
x_k
y_j
y_k
yp_jk
yq_jk
yr_j1
yr_j2
yr_j3
yr_j4
yr_k1
yr_k2
yr_k3
yr_k4
ys_j1
ys_j2
ys_j3
ys_j4
ys_k1
ys_k2
ys_k3
ys_k4
End
