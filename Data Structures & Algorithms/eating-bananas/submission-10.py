class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #[1, 4, 3, 2] h = 9
        # 1 <= k = max(values)
        low = 1
        high = max(piles)
        #0, 1, 2, 3, 4
        ans = max(piles)
        while low <= high:
            mid = (low + high) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p/mid)
            
            if hours > h:
                low = mid + 1
            else:
                ans = mid 
                high =  mid - 1
        return ans 
                
             

        