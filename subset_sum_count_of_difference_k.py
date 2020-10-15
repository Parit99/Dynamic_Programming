#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:48:55 2020

@author: shreeji
"""

arr=[1,1,2,3]
diff=1
sumpass=int((diff+sum(arr))/2)
print(sumpass)
def countsubset(arr,s):
    row=len(arr)
    t=[[0 for i in range(s+1)] for j in range(0,row+1)]
    for i in range(0,row+1):
        for j in range(0,s+1):
            if(j==0):
                t[i][j]=1
    for i in range(1,row+1):
        for j in range(1,s+1):
            if(arr[i-1]<=j):
                t[i][j]=t[i-1][j]+t[i-1][j-arr[i-1]]
            else:
                t[i][j]=t[i-1][j]
    return t,t[row][s]
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
a,ans=countsubset(arr,sumpass)
print('Count of ways for diff K is ',ans)
printmat(a)