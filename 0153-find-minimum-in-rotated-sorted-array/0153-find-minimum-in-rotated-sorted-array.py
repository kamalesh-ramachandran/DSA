class Solution:
    def findMin(self, nums: list[int]) -> int:
        low=0
        high=len(nums)-1
        answer=nums[0]
        while low <= high:
            mid= (low+high)//2

            if nums[mid] <= nums[high]:
                answer=min(answer,nums[mid])
                high=mid-1
            else:
                answer=min(answer,nums[low])
                low=mid+1
        return answer
            

        