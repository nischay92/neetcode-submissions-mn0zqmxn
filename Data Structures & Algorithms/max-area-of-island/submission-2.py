class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        maxArea = 0
        visit = set()

        if not grid:
            return 0

        def dfs(r , c):
            area = 0
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r , c) in visit or grid[r][c] == 0):
                return 0
            visit.add((r , c))
            return( 1 + (dfs(r + 1, c) +
                         dfs(r - 1, c) + 
                         dfs(r , c + 1) +
                         dfs(r , c - 1)))
            

        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r , c))
        return maxArea
