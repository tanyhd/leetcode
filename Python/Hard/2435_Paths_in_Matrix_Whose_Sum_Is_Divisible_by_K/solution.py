from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        return Solution.explore(0, 0, grid, 0, k, {})


    def explore(r, c, grid, rem, k, memo):
        if not Solution.inbound(r, c, grid):
            return 0
        
        mod = 10**9 + 7
        rem = (rem + grid[r][c]) % k
        key = (r, c, rem)
        if key in memo:
            return memo[key]
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            if rem == 0:
                return 1
            return 0
        
        down = Solution.explore(r+1, c, grid, rem, k, memo)
        right = Solution.explore(r, c+1, grid, rem, k, memo)
        
        memo[key] = (down + right) % mod
        return memo[key]
    

    def inbound(r, c, grid):
        rInbound = r >= 0 and r < len(grid)
        cInbound = c >= 0 and c < len(grid[0])
        return rInbound and cInbound