class Solution:
    def searchRange(self, num: list[int], target: int) -> list[int]:
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

        return[first,last]