class Solution:
    def removeDuplicates(self, num: List[int]) -> int:
        slow=0
        for fast in range(1,len(num)):
            if(num[slow] != num[fast]):
                slow+=1
                num[slow]=num[fast]
        return slow+1
        