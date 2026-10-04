class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for num in num_set:
            if (num - 1) not in num_set:
                curr = num
                streak = 1
                while (curr + 1) in num_set:
                    streak += 1
                    curr = curr + 1
                res = max(streak, res)
        return res 
        