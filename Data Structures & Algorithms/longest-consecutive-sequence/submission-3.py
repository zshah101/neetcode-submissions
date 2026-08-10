class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #[2,10,3,4,6,19,5]
        nums.sort()
        count = 1
        longest = 1
        if not nums:
            return 0
        
        #[2,3,4,5,6,10,19]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                count += 1
            else:
                longest = max(count, longest)
                count = 1
        return max(longest, count)

        