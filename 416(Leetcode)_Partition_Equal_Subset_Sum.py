#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:30:41 2020

@author: shreeji
"""

def subsetsum(arr,s):
  row=len(arr)
  t=[[False for i in range(0,s+1)] for j in range(0,row+1)]
  for i in range(0,row+1):
    for j in range(0,s+1):
      if(j==0):
        t[i][j]=True
  for i in range(1,row+1):
    for j in range(1,s+1):
      if(arr[i-1]<=j):
        t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
      else:
        t[i][j]=t[i-1][j] 
  return t[row][s]
  
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
      
      s=sum(nums)
      if((s&1)==1):
        return False
      else:
        s=s>>1
        ans=subsetsum(nums,s)
        return ans