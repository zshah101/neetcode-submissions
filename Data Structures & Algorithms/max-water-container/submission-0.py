class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                length = j - i
                width = min(heights[j], heights[i])
                area = length * width
                res = max(res, area)
        return res
        