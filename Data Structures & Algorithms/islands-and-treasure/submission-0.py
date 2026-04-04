class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        inf = 2147483647
        def bfs(r,c):
            visited = set()
            queue = deque()
            queue.append([r,c])
            visited.add((r,c))

            length = 0

            while queue:
                for x in range(len(queue)):
                    cr,cc = queue.popleft()
                    if grid[cr][cc] == 0:
                        return length
                    else:
                        directions = [[-1,0],[1,0],[0,-1],[0,1]]

                        for dr,dc in directions:
                            if min(cr + dr, cc + dc) >= 0 and cr + dr < rows and cc + dc < cols and (cr + dr, cc + dc) not in visited and grid[cr+dr][cc+dc] != -1:
                                queue.append([cr + dr, cc + dc])
                                visited.add((cr + dr, cc + dc))

                length += 1
            
            return length

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == inf:
                    grid[r][c] = bfs(r,c)


# visited, queue, length
# add original r,c to queue
# pop from queue, if 0 return length 
# else check neighbors, if in bounds, not in visited, if not -1, add to queue

