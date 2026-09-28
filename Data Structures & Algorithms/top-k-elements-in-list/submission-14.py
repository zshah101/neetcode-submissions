class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[1, 2, 2, 3, 3, 3] -> k = 2
        # bucket sort
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        #[[], [], [], []]

        for num, count in seen.items():
            bucket[count].append(num)
        # [[0], [1], [2], [3]]

        res = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res 
        
