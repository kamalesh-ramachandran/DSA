class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        answer=high
        while low <=high:
            split=(low+high)//2

            groups=1
            temp_sum=0
            for num in nums:
                if temp_sum + num > split:
                    groups+=1
                    temp_sum=0
                temp_sum+=num
            
            if groups<=k:
                answer=split
                high=split-1
            else:
                low=split+1
        return answer

                    
        