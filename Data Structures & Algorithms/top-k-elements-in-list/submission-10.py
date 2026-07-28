import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        heap = []
        for num, count in count.items() :
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for count, num in heap:
            res.append(num) 
        return res
