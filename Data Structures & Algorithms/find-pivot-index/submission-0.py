class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        
        left_value = 0
        for i in range(len(nums)):
            left_sum[i] = left_value
            left_value += nums[i]
        right_value = 0
        for i in range(len(nums)-1, -1, -1):
            right_sum[i] = right_value
            right_value += nums[i]
        
        
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1