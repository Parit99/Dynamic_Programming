#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:50:27 2020

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
                t[i][j]=0
    for i in range(0,m+1):
        if(t[i][n]==1):
            t[m][n]=1
    return t,t[m][n]
def printmat(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            print(arr[i][j],end=" ")
        print()
a,ans=dplcs(x,y,m,n)
print('Answer :: ',ans)
printmat(a)