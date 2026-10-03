class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1, 8] [2, 7] [4, 9], [6, 9]]
        intervals.sort()
        output = [intervals[0]] #[1,8]

        for start, end in intervals[1:]:
            prev = output[-1][1]
            if prev >= start:
                output[-1][1] = max(prev, end)
            else:
                output.append([start, end])
        return output


        