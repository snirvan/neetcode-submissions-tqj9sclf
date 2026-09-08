from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0

        while fresh != 0 and queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                r = curr[0]
                c = curr[1]

                grid[r][c] == 2

                directions = [[-1,0],[1,0],[0,-1],[0,1]]

                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visit:
                        queue.append((nr,nc))
                        visit.add((nr,nc))
                        fresh -= 1
            minutes += 1
        
        if fresh == 0:
            return minutes
        return -1



    # only visit and add to queue if not out of bounds, if g[r][c] = 1
# traverse the grid make queue of all rotting fruit
# traverse grid make array of all fresh fruit
# return minutes once if queue is empty and fresh fruit is empty
# return -1 if queue is empty by fresh fruit is not empty

