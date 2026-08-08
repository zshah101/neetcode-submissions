import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        
        hours = 0
        while low <= high:
            mid = (low + high) // 2

            #k = mid = 5
            for p in piles:
                hours += math.ceil(p/mid)

            if hours <= h:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
            hours = 0
        return ans


            

            
            
