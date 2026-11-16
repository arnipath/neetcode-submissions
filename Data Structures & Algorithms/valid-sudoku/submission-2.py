class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_squares = {}
        for i in range(9):
            seen_row = set()
            seen_col = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen_row:
                        return False
                    seen_row.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in seen_col:
                        return False
                    seen_col.add(board[j][i])
                if board[i][j] != ".":
                    square = (i // 3, j // 3)
                    if square not in seen_squares:
                        seen_squares[square] = set()
                    if board[i][j] in seen_squares[square]:
                        return False
                    seen_squares[square].add(board[i][j])
        return True