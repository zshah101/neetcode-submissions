class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        colms = len(heights[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            visited.add((r,c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr >= 0 and
                    nc >= 0 and 
                    nr < rows and 
                    nc < colms and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, visited)
                    

        for c in range(colms):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, colms - 1, atlantic)
        
        result = []
        for r in range(rows):
            for c in range(colms):
                if (r, c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
                
        return result 