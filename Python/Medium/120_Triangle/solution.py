class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        return Solution.explore(0, 0, triangle, {})


    def explore(r, c, grid, memo):
        if not Solution.inbound(r, c, grid):
            return 0
        
        key = (r, c)
        if key in memo:
            return memo[key]

        left = Solution.explore(r + 1, c, grid, memo)
        right = Solution.explore(r + 1, c + 1, grid, memo)
        memo[key] = grid[r][c] + min(left, right)
        return memo[key]


    def inbound(r, c, grid):
        rInbound = r >= 0 and r < len(grid)
        if not rInbound:
            return False
        cInbound = c >= 0 and c < len(grid[r])
        return cInbound
        