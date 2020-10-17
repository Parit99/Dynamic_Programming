#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:26:13 2020

@author: shreeji
"""

coin=[1,2,3]

val=6
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
def uknapsack(coin,val):
    row=len(coin)
    t=[[0 for i in range(0,val+1) ] for j in range(0,row+1)]
    for i in range(0,row+1):
        for j in range(0,val+1):
            if(j==0):
                t[i][j]=1
    for i in range(1,row+1):
        for j in range(1,val+1):
            if(coin[i-1]<=j):
                t[i][j]=t[i][j-coin[i-1]]+t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t,t[row][val]
a,ans=uknapsack(coin,val)
print('Number of ways  ::',ans)
printmat(a)