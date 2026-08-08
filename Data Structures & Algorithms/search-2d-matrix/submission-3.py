class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        colms = len(matrix[0])

        top = 0
        bottom = rows - 1
        target_row = -1
        while top <= bottom:
            middle = (top + bottom) // 2

            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][colms - 1]:
                 top = middle + 1
            else:
                target_row = middle
                break

        if target_row == -1: return False 

        left = 0
        right = colms - 1
        while left <= right:
            mid = (left + right) // 2

            if target > matrix[target_row][mid]:
                left = mid + 1
            elif target < matrix[target_row][mid]:
                right = mid - 1
            else:
                return True
        return False 

        