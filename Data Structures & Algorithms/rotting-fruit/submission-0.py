from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visit = set()
        queue = deque()
        fresh_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    visit.add((r,c))
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh_count += 1

        Rows = len(grid)
        Cols = len(grid[0])
            
        minutes = 0 

        while queue:
            rotted_this_minute = False
            for i in range(len(queue)):
                minus_count = 0
                curr = queue.popleft()
                r = curr[0]
                c = curr[1]

                grid[r][c] = 2

                directions = [[-1,0],[1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    if min(r+dr,c+dc) >= 0 and r+dr < Rows and c+dc < Cols and grid[r+dr][c+dc] == 1 and (r+dr,c+dc) not in visit:
                        visit.add((r+dr,c+dc))
                        queue.append((r+dr,c+dc))
                        fresh_count -= 1
                        rotted_this_minute = True
            if rotted_this_minute:
                minutes += 1
            
        if fresh_count == 0: 
            return minutes
        else:
            return -1



    # only visit and add to queue if not out of bounds, if g[r][c] = 1
# traverse the grid make queue of all rotting fruit
# traverse grid make array of all fresh fruit
# return minutes once if queue is empty and fresh fruit is empty
# return -1 if queue is empty by fresh fruit is not empty

