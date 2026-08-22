class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        res=0
        maxi=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            if freq[i] >= len(nums)/2:
                maxi=freq[i]
                res=i
        return res
        