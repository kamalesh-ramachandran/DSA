class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low <= high:
            capacity=(low+high)//2

            required_days=1
            load=0
            for weight in weights:
                if load + weight > capacity:
                    required_days+=1
                    load=0
                load+=weight
            if required_days <= days:
                high=capacity-1
            else:
                low=capacity+1
        return low    