class Solution:
    def topKFrequent(self, nums, k):
        count = []
        visited = set()

        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            
            counts = 0

            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    counts += 1
                
            count.append((counts, nums[i]))
            visited.add(nums[i])

        sorted_nums = sorted(count, reverse=True)

        result = []
        for count, num in sorted_nums:
            result.append(num)
            
        return result[:k]
        
                