#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:26:13 2020

@author: shreeji
"""

wt=[1,2,3,5]
profit=[5,10,5,15]
W=10
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
def uknapsack(wt,profit,W):
    row=len(wt)
    t=[[-1 for i in range(0,W+1) ] for j in range(0,row+1)]
    for i in range(0,row+1):
        for j in range(0,W+1):
            if(j==0 or i==0):
                t[i][j]=0
    for i in range(1,row+1):
        for j in range(1,W+1):
            if(wt[i-1]<=j):
                t[i][j]=max(profit[i-1]+t[i][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t,t[row][W]
a,ans=uknapsack(wt,profit,W)
print('Profit for unbounded knapsack ::',ans)
printmat(a)