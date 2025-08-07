class Solution:
    def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
        moves = len(fruits) - 1
        firstC = Solution.explore1(0, 0, fruits, moves)
        secondC = Solution.explore2(0, moves, fruits, moves, {})
        thirdC = Solution.explore3(moves, 0, fruits, moves, {})

        total = firstC + secondC + thirdC
        return total


    def explore1(r, c, grid, moves):
        lastR = len(grid) - 1
        lastC = lastR
        if moves == 0 and r == lastR and c == lastC:
            return grid[lastR][lastC]
        
        path = Solution.explore1(r+1, c+1, grid, moves-1)
        return path + grid[r][c]
    
    def explore2(r, c, grid, moves, memo):
        if not Solution.inboundTop(r, c, grid) or moves < 0:
            return 0
        
        if (r,c) in memo:
            return memo[(r,c)]
        lastR = len(grid) - 1
        lastC = lastR
        if moves == 0 and r == lastR and c == lastC:
            return grid[lastR][lastC]
        
        maxCount = 0
        path1 = Solution.explore2(r+1, c-1, grid, moves-1, memo)
        path2 = Solution.explore2(r+1, c, grid, moves-1, memo)
        path3 = Solution.explore2(r+1, c+1, grid, moves-1, memo)

        maxCount = max(maxCount, path1 + grid[r][c])
        maxCount = max(maxCount, path2 + grid[r][c])
        maxCount = max(maxCount, path3 + grid[r][c])
        memo[(r,c)] = maxCount
        return maxCount

    def explore3(r, c, grid, moves, memo):
        if not Solution.inboundBot(r, c, grid) or moves < 0:
            return 0
        if (r,c) in memo:
            return memo[(r,c)]
        lastR = len(grid) - 1
        lastC = lastR
        if moves == 0 and r == lastR and c == lastC:
            return grid[lastR][lastC]
        
        maxCount = 0
        path1 = Solution.explore3(r-1, c+1, grid, moves-1, memo)
        path2 = Solution.explore3(r, c+1, grid, moves-1, memo)
        path3 = Solution.explore3(r+1, c+1, grid, moves-1, memo)

        maxCount = max(maxCount, path1 + grid[r][c])
        maxCount = max(maxCount, path2 + grid[r][c])
        maxCount = max(maxCount, path3 + grid[r][c])
        memo[(r,c)] = maxCount
        return maxCount

    def inboundTop(r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid) and c > r

    def inboundBot(r, c, grid):
        return 0 <= r < len(grid) and 0 <= c < len(grid) and r > c