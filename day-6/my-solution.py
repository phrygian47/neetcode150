from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                elif ((board[i][j] in rows[i]) or 
                (board[i][j] in columns[j]) or 
                (board[i][j]in squares[i//3, j//3])):
                    return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                squares[i//3, j//3].add(board[i][j])
        return True