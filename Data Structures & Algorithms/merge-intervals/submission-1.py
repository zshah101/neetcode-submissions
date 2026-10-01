class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #[1, 3] [2, 6] [5, 7] [6, 8]  
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = res[-1][1]

            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        return res 
