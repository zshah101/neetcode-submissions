class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, colms = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            
            grid[r][c] = "0"
            
            while q:
                r, c = q.popleft()
                for row, col in directions:
                    nr = r + row
                    nc = c + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= colms or grid[nr][nc] == "0"):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
            
        for r in range(rows):
            for c in range(colms):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands 

        