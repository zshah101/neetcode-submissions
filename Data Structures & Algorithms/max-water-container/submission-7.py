class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #[1, 7, 2, 5, 4, 7, 3, 6]
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            length = right - left
            height = min(heights[left], heights[right])
            area = length * height
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            res = max(area, res)
        return res 
                

            
        
        
        
        
        