#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:27:19 2019

@author: shreeji
"""

arr=[3,2,4,5]
profit=[5,10,1,6]
weight=9
len_arr=len(arr)
dp=[]
def knapsack(wt,val,W,n):
    if(n==0 or W==0):
        return 0
    if(wt[n-1]<=W):
        return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    elif(wt[n-1]>W):
        return knapsack(wt,val,W,n-1)
total=knapsack(arr,profit,weight,len_arr)
print(total)