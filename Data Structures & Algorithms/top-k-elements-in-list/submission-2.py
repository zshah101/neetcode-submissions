import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #O(1)

        for num in nums: #O(n)
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        buckets = []    #[ [], [],  [1],  [], [], [], [] ]
                        #   0    1    2    3   4   5   6
        
        for i in range(len(nums) + 1):
            buckets.append([]) 
        
        for num, count in count.items():
            buckets[count].append(num)
        
        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

