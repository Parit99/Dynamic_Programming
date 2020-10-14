#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 17:37:47 2020

@author: shreeji
"""

def subsetsum(arr,s):
  row=len(arr)
  t=[[0 for i in range(0,s+1)] for j in range(0,row+1)]
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
  
arr=[2,3,7,8,10]
s=10
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()

t,ans=subsetsum(arr,s)
print(ans)
printmat(t)