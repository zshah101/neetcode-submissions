import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #O(1)
        for num in nums: #O(n)
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        heap = []
        for num, count in count.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for count, num in heap:
            result.append(num)
        return result

        





            


                    



        




