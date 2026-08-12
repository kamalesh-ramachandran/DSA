class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        adds={}
        for index,value in enumerate(nums):
            comp=target - value 
            if comp in adds:
                return [index,adds[comp]]
            adds[value]=index