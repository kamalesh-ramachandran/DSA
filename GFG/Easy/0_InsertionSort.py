"""
Problem Link : https://practice.geeksforgeeks.org/problems/insertion-sort/1
Platform     : GFG
Difficulty   : Easy
"""

class Solution:
    def insertionSort(self, arr):
        n=len(arr)
        for i in range(1,n):
            temp_element=arr[i]
            j=i-1
            while j>=0 and arr[j] > temp_element:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=temp_element
        return arr
        
