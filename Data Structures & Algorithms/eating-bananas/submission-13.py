class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #[1, 4, 3, 2]
        #h = 9,  k = 1
        low = 1
        high = max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2

            hours = 0

            for p in piles:
                hours += math.ceil(p/mid)
            
            if hours > h:
                low = mid + 1
            else:
                res = mid
                high = mid - 1
        return res 


        