"""
Problem Link : https://practice.geeksforgeeks.org/problems/selection-sort/1
Platform     : GFG
Difficulty   : Easy
"""

class Solution: 
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if nums[j] < nums[min_index]:
                    min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]

        return nums
