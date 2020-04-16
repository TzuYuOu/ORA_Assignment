#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:23:34 2020

@author: tzuyuou
"""

import numpy as np

a = np.array([[0.8,0.2,0,0],[0,0,0.2,0.8],[0,1,0,0], [0.8,0.2,0,0]])

b = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0], [0,0,0,1]])

s = np.array([1,0,0,0])

#error = np.ones(4)   
#cnt = 0
#while max(error) > 0.0001:
#    cnt+=1
#    ls = s
#    b = np.dot(b,a)
#    s = np.dot(s,a)
#    error = abs(s-ls)
#    
#print(s)
#print("steady state:\n",b)
#print("Stop iteration time: ",cnt)

for i in range(2):
    b = np.dot(b,a)
    s = np.dot(s,a)
print(s)
    






#for i in range(30):
#    ls = s
#    b = np.dot(b,a)
#    s = np.dot(b,s)
#    error = abs(s-ls)
#    print(error)
#    if any(error) < 0.0001:
#        break
#    
#print(s,i)