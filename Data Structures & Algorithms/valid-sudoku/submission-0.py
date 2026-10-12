class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for colm in range(9):
            seen = set()
            for i in range(9):
                if board[i][colm] == ".":
                    continue
                if board[i][colm] in seen:
                    return False
                seen.add(board[i][colm])

        for square in range(9):
            seen = set()

            row = (square // 3) * 3
            colm = (square % 3) * 3

            for i in range(3):
                for j in range(3):
                    value = board[row + i][colm + j]

                    if value == ".":
                        continue

                    if value in seen:
                        return False

                    seen.add(value)

        return True