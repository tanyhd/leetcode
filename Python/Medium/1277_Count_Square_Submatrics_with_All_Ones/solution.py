class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        totalCount = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                totalCount += Solution.explore(r, c, matrix, {})
        return totalCount


    def explore(r, c, matrix, memo):
        if not Solution.inbound(r, c, matrix):
            return 0

        if (r,c) in memo:
            return memo[(r,c)]

        if matrix[r][c] == 0:
            return 0
        
        up = Solution.explore(r-1, c, matrix, memo)
        left = Solution.explore(r, c-1, matrix, memo)
        diagonal = Solution.explore(r-1, c-1, matrix, memo)
        size = 1 + min(up, left, diagonal)
        
        memo[(r,c)] = size
        return size

    def inbound(r, c, matrix):
        rInbound = r >= 0 and r < len(matrix)
        cInbound = c >= 0 and c < len(matrix[0])
        return rInbound and cInbound