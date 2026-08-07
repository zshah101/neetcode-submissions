class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        colms = len(matrix[0])

        top = 0
        bottom = rows - 1
        target_row = -1
        while top <= bottom:
            middle = (top + bottom) // 2

            first = matrix[middle][0]
            last = matrix[middle][colms - 1]

            if target > last:
                top = middle + 1
            elif target < first:
                bottom = middle - 1
            else:
                target_row = middle
                break
        if target_row == -1:
            return False
        
        left = 0
        right = colms - 1
        while left <= right:
            mid = (left + right) // 2
            curr = matrix[target_row][mid]

            if curr == target:
                return True
            elif curr > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        