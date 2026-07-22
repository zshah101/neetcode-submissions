import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} #{(2:1), (2:2), (3:3), (1:4)}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        heap = [] #1:4, 2:1, 2:2, 3:3
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for count, num in heap:
            result.append(num)
        return result
        