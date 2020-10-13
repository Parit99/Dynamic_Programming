#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:09:32 2019

@author: shreeji
"""
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
def subsetsum(arr,sumval,row):
    t=[[False for i in range(0,sumval+1)] for j in range(0,row+1)]
    for i in range(0,row+1):
        for j in range(0,sumval+1):
            if(j==0):
                t[i][j]=True
    for i in range(1,row+1):
        for j in range(1,sumval+1):
            if(arr[i-1]<=j):
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t,t[row][sumval]
arr=[2,3,7,8,10]
sumval=11 #can take value such as 15,10,12,18,17 to verify
row=len(arr)
t,ans=subsetsum(arr,sumval,row)
print('Answer (T or F) is :: ',ans)
'''If you want to visualize the matrix '''
#printmat(t)