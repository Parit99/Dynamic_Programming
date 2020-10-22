#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:16:41 2019

@author: shreeji
"""

x='abcdefbc'
y='acbe' #ans=3 3 ans acb,ace,abe

m=len(x)
n=len(y)
def dplcs(x,y,m,n):
    t=[[-1 for i in range(0,n+1)]for j in range(0,m+1)]
    for i in range(0,n+1):
        t[0][i]=0
    for i in range(0,m+1):
        t[i][0]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(x[i-1]==y[j-1]):
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i][j-1],t[i-1][j])
    return t,t[m][n]
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
a,ans=dplcs(x,y,m,n)
print('Answer :: ',ans)
printmat(a)