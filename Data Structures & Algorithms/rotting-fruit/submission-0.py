class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        fresh = 0
        rows, colms = len(grid), len(grid[0])

        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        for r in range(rows):
            for c in range(colms):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for r_d, c_d in directions:
                    row = r + r_d 
                    colm = c + c_d
                    
                    if (row < 0 or colm < 0 or row >= rows or colm >= colms or grid[row][colm] != 1):
                        continue
                    grid[row][colm] = 2
                    q.append([row, colm])
                    fresh -= 1

            time += 1
        return time if fresh == 0 else -1 




            
        