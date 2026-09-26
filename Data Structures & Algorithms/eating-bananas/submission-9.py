import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #[1, 4, 3, 2] h = 9
        # 1 <= k <= max(piles)
        left = 1
        right = max(piles)
        ans = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hours = 0

            for num in piles:
                if num == 0:
                    continue
                hours += math.ceil(num/mid)
            if hours > h:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans  
            

            

                

        