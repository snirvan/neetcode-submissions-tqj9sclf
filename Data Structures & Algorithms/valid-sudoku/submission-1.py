class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

     # make a set for each row lop through row if num already in set return false
     # make a set for each row lop through row if num already in set return false
     # make a set for each square and if num already in set return false
     # return true

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        board_len = len(board)
        
        for r in range(board_len):
            for c in range(board_len):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r] or num in cols[c] or num in squares[(r//3,c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True