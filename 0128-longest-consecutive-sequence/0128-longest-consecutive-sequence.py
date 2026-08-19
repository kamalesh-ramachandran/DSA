class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        sequence=set(nums)
        for value in sequence:
            if value - 1 not in sequence:
                current=value
                count=1
                while current+1 in sequence:
                    current=current+1
                    count+=1
                longest=max(longest,count)   
        return longest

            

        