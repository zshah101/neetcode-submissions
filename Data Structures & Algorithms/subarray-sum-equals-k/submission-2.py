class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #[2, -1, 1, 2] k = 2
        pref_sum = {0: 1}

        res = 0
        curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k

            if diff in pref_sum:
                res += pref_sum[diff]
            
            if curSum in pref_sum:
                pref_sum[curSum] += 1
            else:
                pref_sum[curSum] = 1
        return res 
