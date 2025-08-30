class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        output = []
        side = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r == 0:
                    ls = []
                    Solution.explore(r, c, mat, ls)
                    Solution.appendOutput(output, side, ls)
                    side += 1
                elif c == len(mat[0]) - 1 and r != 0:
                    ls = []
                    Solution.explore(r, c, mat, ls)
                    Solution.appendOutput(output, side, ls)
                    side += 1
        return output
    
    def explore(r, c, mat, ls):
        if not Solution.inbound(r, c, mat):
            return
        ls.append(mat[r][c])
        Solution.explore(r+1, c-1, mat, ls)

    
    def inbound(r, c, mat):
        rInbound = r >= 0 and r < len(mat)
        cInbound = c >= 0 and c < len(mat[0])
        return rInbound and cInbound


    def appendOutput(output, side, ls):
        if side % 2 == 0:
            while len(ls) != 0:
                temp = ls.pop()
                output.append(temp)
        else:
            output += ls