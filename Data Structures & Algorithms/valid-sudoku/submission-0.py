class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        setArr = [set() for _ in range(9)]
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]

        for row in range(0,len(board)):
            for col in range(0,len(board)):
                squareIndex = int((row // 3) * 3 + (col // 3))
                spot = board[row][col]
                if spot.isdigit():
                    if int(spot) in setArr[squareIndex] or int(spot) in rowSets[row] or int(spot) in colSets[col]:
                        return False
                    setArr[squareIndex].add(int(spot))
                    rowSets[row].add(int(spot))
                    colSets[col].add(int(spot))
        
        return True

