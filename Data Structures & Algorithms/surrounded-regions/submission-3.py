class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # iterate through all boundry points
        # if 0 run BFS that turns O into T
        # go through whole board and change any O into X and any T into O

        rows = len(board)
        cols = len(board[0])
        q = deque()

        def bfs():
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            while q:
                r,c = q.popleft()

                for dr, dc in directions:
                    nr,nc = r+dr, c+dc

                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                        board[nr][nc] = "T"
                        q.append((nr,nc))
            
        
        # start bfs from all boundary 0
        for r in range(rows):
            if board[r][0] == "O":
                board[r][0] = "T"
                q.append((r,0))
            if cols > 1 and board[r][cols-1] == "O":
                board[r][cols-1] = "T"
                q.append((r,cols-1))
        
        for c in range(cols):
            if board[0][c] == "O":
                board[0][c] = "T"
                q.append((0,c))
            if rows > 1 and board[rows-1][c] == "O":
                board[rows-1][c] = "T"
                q.append((rows-1,c))

        # 2nd pass, convert O -> X, T -> O 

        bfs()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


