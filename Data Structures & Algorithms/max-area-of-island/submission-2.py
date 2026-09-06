class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        max_area = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= Rows or c >= Cols or grid[r][c] == 0:
                return 0
            if grid[r][c]:
                grid[r][c] = 0
                return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c+1) + dfs(r,c-1) + dfs(r,c+1)

        
        for r in range(Rows):
            for c in range(Cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        return max_area