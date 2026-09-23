class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums.sort() 
        res = 1
        
        visited = set() 
        for i in range(len(nums)):
            if i in visited:
                continue

            count = 1
            current = nums[i]
            visited.add(i)

            for j in range(i+1, len(nums)):
                if nums[j] == current:
                    continue
                
                if nums[j] == current + 1:
                    count += 1
                    current = nums[j]
                    visited.add(j)
                else:
                    break

            res = max(res, count)
        return res
                



        


        