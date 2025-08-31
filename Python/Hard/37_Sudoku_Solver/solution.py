class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        numMap = {}
        numFilled = set()
        
        while len(numFilled) < 81:
            for r in range(9):
                for c in range(9):
                    if board[r][c] != ".":
                        numFilled.add((r,c))
                    if board[r][c] == ".":
                        key = (r,c)
                        if (r,c) not in numMap:
                            numMap[(r, c)] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        Solution.checkRow(r, c, board, numMap, key)
                        Solution.checkCol(r, c, board, numMap, key)
                        Solution.checkBox(r, c, board, numMap, key)
        return board
       


    def checkRow(r, c, board, numMap, key):
        for i in range(len(board)):
            if board[r][i] != "." and board[r][i] in numMap[key]:
                numMap[key].remove(board[r][i])
                Solution.fillNum(board, numMap, key)

    def checkCol(r, c, board, numMap, key):
        for i in range(len(board[0])):
            if board[i][c] != "." and board[i][c] in numMap[key]:
                numMap[key].remove(board[i][c])
                Solution.fillNum(board, numMap, key)

    def checkBox(r, c, board, numMap, key):
        r = (r // 3) * 3
        c = (c // 3) * 3

        for i in range(3):
            for j in range(3):
                cR, cC = r + i, c + j
                if board[cR][cC] != "." and board[cR][cC] in numMap[key]:
                    numMap[key].remove(board[cR][cC])
                    Solution.fillNum(board, numMap, key)

    def fillNum(board, numMap, key):
        if len(numMap[key]) == 1:
            num = numMap[key][0]
            r, c = key
            board[r][c] = num