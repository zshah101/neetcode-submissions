class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = []
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                continue

            count = 0
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1 
            
            counts.append((count, nums[i]))
            seen.add(nums[i])

        sorted_nums = sorted(counts, reverse=True)

        res = []
        for i, n in sorted_nums:
            res.append(n)
        return res[:k]
                
                         
        