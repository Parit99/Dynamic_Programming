#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:07:54 2019

@author: shreeji
"""

wt=[3,2,4,5]
val=[5,10,1,6]
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
def findmaxprofit(wt,val,W):
    n=len(wt)
    t=[[-1 for i in range(0,W+1)]for j in range(0,n+1)]
    for i in range(0,n+1):
        for j in range(0,W+1):
            if(i==0 or j==0):
                t[i][j]=0
    for i in range(1,n+1):
        for j in range(1,W+1):
            if(wt[i-1]<j):
                t[i][j]=max(t[i-1][j],val[i-1]+t[i-1][j-wt[i-1]])
            else:
                t[i][j]=t[i-1][j]
    return t,t[n][W]
W=9
arr,profit=findmaxprofit(wt,val,W)
print(profit)
printmat(arr)