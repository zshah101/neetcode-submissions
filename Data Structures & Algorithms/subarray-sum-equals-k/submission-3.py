class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pMap = {0:1}

        res = 0

        prefix = 0
        for num in nums:
            prefix += num
            diff = prefix - k

            if diff in pMap:
                res += pMap[diff]
            
            if prefix in pMap:
                pMap[prefix] += 1
            else:
                pMap[prefix] = 1
        return res 
