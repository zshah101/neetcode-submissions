class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        nums.sort()

        res = []
        for k in range(len(nums)):
            if k and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = len(nums) - 1

            while i < j:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return res 
                    
                    
                

            
            

        
        
        