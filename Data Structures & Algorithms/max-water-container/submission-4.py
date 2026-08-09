class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        i = 0 
        j = len(heights) - 1

        while i < j:
            length = j - i
            height = min(heights[i], heights[j])
            area = length * height
            water = max(water, area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return water 


        