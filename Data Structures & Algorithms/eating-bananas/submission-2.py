import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1 
        high = max(piles)
        ans = high

        while low <= high:
            mid =(low + high) // 2
            
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)


            if hours <= h: #this statment is to check if koko finished in time, so are we in bounds
                ans = mid
                high = mid - 1 #this, because we know it worked for this (everything bigger will work too), so since we need the min val we go down lower to find smaller. but at the point where hourse > h (we will go out of guards and hence that will be false)
            else: #this means its too big (so k is to slow or small so we find the bigger/faster eating value)
                low = mid + 1
        return ans




            

            
            
