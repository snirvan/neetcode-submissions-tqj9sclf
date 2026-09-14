class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        output = []

        def dfs(r,c,visited,prevHeight):
            if min(r,c) >= 0 and r < rows and c < cols and (r,c) not in visited and heights[r][c] >= prevHeight: 
                visited.add((r,c))

                dfs(r-1,c,visited,heights[r][c])
                dfs(r+1,c,visited,heights[r][c])
                dfs(r,c-1,visited,heights[r][c])
                dfs(r,c+1,visited,heights[r][c])


        for r in range(rows):
            dfs(r,0,pacific,0)
            dfs(r,cols-1,atlantic,0)
        
        for c in range(cols):
            dfs(0,c,pacific,0)
            dfs(rows-1,c,atlantic,0)
    
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    output.append([r,c])
    
        return output


# make pacific set and atlantic set
# start dfs from all border squares, give them the set of the ocean they border
# if in bounds and height >= curr height and not visited respective set: then explore neighbor otherwise return


