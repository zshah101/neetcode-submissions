class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #[1, 2, 0, 1, 0]
        goal = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False 