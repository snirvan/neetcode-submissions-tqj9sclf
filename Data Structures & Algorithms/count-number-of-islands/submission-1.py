class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    
        islands = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0":
                return
        
            if grid[r][c] == "1":
                grid[r][c] = "0"
            

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        
        return islands
                    
        


# iterate through the grid
# if you find g[r][c] = 1:
    # incrament island count
    # run dfs on that location:
        #base case: if out of bounds, or 0, return,
        # if g[r][c] == 1:
            #set g[r][c] = 0
        # go in all 4 directions