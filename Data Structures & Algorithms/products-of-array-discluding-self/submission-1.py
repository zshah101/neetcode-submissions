class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n #[1,1,1,1] - [1,2,8,16]

        left_product = 1 #1,2,8,16
        for i in range(n): #0,1,2,3
            res[i] = left_product #1,1,2,8
            left_product *= nums[i] #1,2,8,16
        right_product = 1
        for i in range(n -1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        
        return res

