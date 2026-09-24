class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        hours = right

        while left <= right:
            mid_k = (left + right) // 2
            min_hours = 0

            for value in piles:
                min_hours += math.ceil(value/mid_k)
            if min_hours > h:
                left = mid_k + 1
            else:
                hours = min(hours, mid_k)
                right = mid_k - 1
        return hours                
                
                 
                

        
        