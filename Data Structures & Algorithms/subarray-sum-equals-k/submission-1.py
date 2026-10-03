class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefix_sum = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            if diff in prefix_sum:
                res += prefix_sum[diff]
            if curSum in prefix_sum:
                prefix_sum[curSum] += 1
            else:
                prefix_sum[curSum] = 1
        return res            
