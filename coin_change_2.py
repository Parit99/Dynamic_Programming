#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:03:29 2020

@author: shreeji
"""
from  math import inf
arr=[5,3,2]
s=5
row=len(arr)
t=[[inf for i in range(0,s+1)] for j in range(0,row+1)]
for i in range(0,row+1):
    for j in range(0,s+1):
        if(i==0):
            t[i][j]=inf
        if(i>0 and j==0):
            t[i][j]=0
def printmat(arr):
    for  i  in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
for i in range(1,s+1):
    if(i%arr[0]==0):
        t[1][i]=i//arr[0]
for i in range(2,row+1):
    for j in range(1,s+1):
        if(arr[i-1]<=j):
            t[i][j]=min(t[i][j-arr[i-1]]+1,t[i-1][j])
        else:
            t[i][j]=t[i-1][j]
        
printmat(t)