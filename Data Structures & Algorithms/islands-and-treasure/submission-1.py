class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))

        visited = set()
        while queue:
            r,c = queue.popleft()

            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r+dr, c+dc

                if nr < 0 or nr >= rows or nc <0 or nc >= cols:
                    continue
                
                if grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr,nc))

        
        return


                #0
                #inf
                # anything else we dont traverse




# visited, queue, length
# add original r,c to queue
# pop from queue, if 0 return length 
# else check neighbors, if in bounds, not in visited, if not -1, add to queue

