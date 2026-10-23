"""
Problem Link : https://practice.geeksforgeeks.org/problems/bubble-sort/1
Platform     : GFG
Difficulty   : Easy
"""

class Solution:
    def bubbleSort(self,num):
        n=len(num)
        for i in range(n):
            swapped=False
            for j in range(n-1-i):
                if num[j] > num[j+1]:
                    num[j],num[j+1]=num[j+1],num[j]
                    swapped=True
            if not swapped:
                break
        return num

        
