class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        answer=-1
        while low <= high:
            mid =(low+high)//2
            if mid * mid <=x:
                answer=mid
                low=mid+1
            else:
                high=mid-1
        return answer

        