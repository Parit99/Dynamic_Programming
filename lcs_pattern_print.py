#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:06:53 2019

@author: shreeji
"""

x='abcdefbc'
y='aced' #ans=3 3 ans acb,ace,abe

#x='abcdfg'
#y='acfg'
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
t,ans=dplcs(x,y,m,n)
print('Answer :: ',ans)
printmat(t)
i=m
j=n
string=""
while(i>0 and j>0):
    if(x[i-1]==y[j-1]):
        string=string+x[i-1]
        i=i-1
        j=j-1
    else:
        if(t[i-1][j]>t[i][j-1]):
            i=i-1
        else:
            j=j-1
print('Resultant String :: ',string[::-1])






