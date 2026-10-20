"""
Problem Link : https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1
Platform     : GFG
Difficulty   : Medium
"""

class Solution:
    def countFreq(self, num, target):
                low=0
                high=len(num)-1
                first=-1

                while low <= high:
                   mid= (low + high) // 2
                   if num[mid] == target:
                      first=mid
                      high=mid-1
                   if target < num[mid]:
                       high = mid - 1
                   if target > num[mid]:
                       low = mid +1
               
                low=0
                high=len(num)-1
                last=-1
                while low <= high:
                   mid= (low + high) // 2
                   if num[mid] == target:
                      last=mid
                      low=mid+1
                   if target < num[mid]:
                       high = mid - 1
                   if target > num[mid]:
                       low = mid +1
                       
                if(first == -1 or last == -1):
                    return 0
                else:
                    return (last - first) +1
        
