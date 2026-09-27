class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, colms = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] #this is all the four boundaries
    
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for r,c in directions:
                    new_row = row + r
                    new_colm = col + c
                    if (new_row < 0 or new_colm < 0 or new_row >= rows or new_colm >= colms or grid[new_row][new_colm] == "0"):
                        continue
                    q.append((new_row, new_colm))
                    grid[new_row][new_colm] = "0"


        for r in range(rows):
            for c in range(colms):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands 

        
        