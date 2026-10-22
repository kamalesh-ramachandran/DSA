import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low=1
        high=max(piles)
        answer=-1
        while low<=high:
            speed = (low+high)//2

            hours=0
            for pile in piles:
                hours+= math.ceil(pile/speed)
            
            if hours<=h:
                answer=speed
                high=speed-1
            else:
                low=speed+1
        return answer