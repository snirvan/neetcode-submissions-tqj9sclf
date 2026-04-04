class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r,c,i,word,visit):
            if min(r,c) < 0 or r == len(board) or c == len(board[0]) or (r,c) in visit:
                return False
            if i == len(word) - 1 and board[r][c] == word[i]:
                return True

            if board[r][c] != word[i]:
                return False

            visit.add((r,c))

            hasPath = dfs(r+1,c,i+1,word,visit) or dfs(r-1,c,i+1,word,visit) or dfs(r,c+1,i+1,word,visit) or dfs(r,c-1,i+1,word,visit)
            visit.remove((r,c))
            return hasPath

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0,word,set()):
                    return True

        return False
        