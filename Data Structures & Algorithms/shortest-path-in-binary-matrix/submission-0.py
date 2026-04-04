from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(grid):
            Rows = len(grid)
            Cols = len(grid[0])
            visit = set()
            queue = deque()
            if grid[0][0] == 1:
                return -1
            visit.add((0,0))
            queue.append((0,0))

            length = 1
        
            while queue:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    r = curr[0]
                    c = curr[1]

                    if curr == (Rows-1, Cols-1) and grid[r][c] == 0:
                        return length
                    
                    directions = [[-1,0], [0,1], [1,0], [0,-1],[-1,-1],[-1,1],[1,1],[1,-1]]

                    for dr,dc in directions:
                        if min(r+dr, c+dc) >= 0 and r+dr < Rows and c + dc < Cols and grid[r+dr][c+dc] == 0 and (r+dr,c+dc) not in visit:
                            visit.add((r+dr,c+dc))
                            queue.append((r+dr,c+dc))
                length+= 1

            return -1

        return bfs(grid)

# if the node is target return length
# otherwise add all neighbors to queue
    # only add if not out of bounds, or not equal to 1, and not visited

