class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        colms = len(heights[0])

        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        def dfs(r, c, ocean, visited):
            if ocean == "pacific":
                if r == 0 or c == 0:
                    return True
            
            if ocean == "atlantic":
                if r == rows - 1 or c == colms - 1:
                    return True

            visited.add((r, c))
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    nr >= 0 and 
                    nc >= 0 and 
                    nr < rows and 
                    nc < colms and 
                    (nr, nc) not in visited and 
                    heights[nr][nc] <= heights[r][c]
                ):
                    if dfs(nr, nc, ocean, visited):
                        return True

            return False 

        result = []

        for r in range(rows):
            for c in range(colms):
                pacific = dfs(r, c, "pacific", set())
                atlantic = dfs(r, c, "atlantic", set())

                if pacific and atlantic:
                    result.append([r, c])

        return result