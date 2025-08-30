class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0:
                    colLst = []
                    if not Solution.checkCol(r, c, board, colLst):
                        return False
                if c == 0:
                    rowLst= []
                    if not Solution.checkRow(r, c, board, rowLst):
                        return False
                if r % 3 == 0 and c % 3 == 0:
                    if not Solution.checkBox(r,c, board):
                        return False
        return True

    def checkRow(r, c, board, ls):
        if not Solution.inbound(r, c, board):
            return True
        if board[r][c] in ls:
            return False
        if board[r][c] != ".":
            ls.append(board[r][c])
        return Solution.checkRow(r, c+1, board, ls)
        
    def checkCol(r, c, board, ls):
        if not Solution.inbound(r, c, board):
            return True
        if board[r][c] in ls:
            return False
        if board[r][c] != ".":
            ls.append(board[r][c])
        return Solution.checkCol(r+1, c, board, ls)

    def checkBox(r, c, board):
        ls = []
        for i in range(0, 3):
            for j in range(0, 3):
                cR = r + i
                cC = c + j
                if board[cR][cC] in ls:
                    return False
                if board[cR][cC] != ".":
                    ls.append(board[cR][cC])
        return True

    def inbound(r, c, board):
        rInbound = r >= 0 and r < len(board)
        cInbound = c >= 0 and c < len(board[0])
        return rInbound and cInbound