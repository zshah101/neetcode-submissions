import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #{(1:1). (2:3), (3:4)}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for num, count in count.items():
            buckets[count].append(num) #[[], [3], [2]]
                                       # 0,   1,    2 
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
                
                    



        




