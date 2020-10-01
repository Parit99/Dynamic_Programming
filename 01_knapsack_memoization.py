#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:10:22 2019

@author: shreeji
"""

arr=[3,2,4,5]
profit=[5,10,1,6]
weight=9
len_arr=len(arr)
dp=[]

for i in range(0,len_arr+1):
    m=[]
    for j in range(0,weight+1):
        m.append(-1)
    dp.append(m)


def knapsack(wt,val,W,n):
    if(n==0 or W==0):
        return 0
    if(dp[n][W]!=-1):
        return dp[n][W]
    if(wt[n-1]<=W):
        dp[n][W]=max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        return dp[n][W]
    elif(wt[n-1]>W):
        dp[n][W]=knapsack(wt,val,W,n-1)
        return dp[n][W]
'''
def knapsack(wt,val,W,n):
    if(n==0 or W==0):
        return 0
    if(wt[n-1]<=W):
        return max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
    elif(wt[n-1]>W):
        return knapsack(wt,val,W,n-1)
'''        
total=knapsack(arr,profit,weight,len_arr)
print(total)