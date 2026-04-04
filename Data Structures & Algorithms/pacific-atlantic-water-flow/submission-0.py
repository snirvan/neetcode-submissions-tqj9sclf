class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        output = []

        def dfs(r,c,visited, prevHeight):

            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or heights[r][c] < prevHeight:
                return
            
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


# make a pacific set and a atlantic set
## run dfs from all border cells dfs(r,c,set):
# add cell to respective set
# if neighbor in bounds, neighbor not in respective set, neighbor cell >= curr cell then explore neighbor otherwise return


