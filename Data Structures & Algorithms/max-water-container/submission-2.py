class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            length = j - i
            height = min(heights[j], heights[i])
            area = length * height
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
            res = max(res, area)
        return res  
    #Time - o(n)
    #Space - o(1)

            