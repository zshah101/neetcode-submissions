class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, colms = len(grid), len(grid[0])
        res = 0

        directions  = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= colms or grid[nr][nc] == "0"):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))            
            

        for r in range(rows):
            for c in range(colms):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        return res 
                

        
        