import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, colms = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))

            grid[r][c] = "0"
            
            while q:
                row, col = q.popleft()
                
                for r, c in directions:
                    n_r = row + r
                    n_c = col + c

                    if (n_r < 0 or n_c < 0 or n_r >= rows or n_c >= colms or grid[n_r][n_c] == "0"):
                        continue

                    grid[n_r][n_c] = "0"
                    q.append((n_r, n_c))
            #
            

        for r in range(rows):
            for c in range(colms):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands