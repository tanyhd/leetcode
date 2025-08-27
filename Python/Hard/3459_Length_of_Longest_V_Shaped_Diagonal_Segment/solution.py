class Solution:
    def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
        directions = {
            "leftTop": (-1, -1),
            "leftBot": (1, -1),
            "rightTop": (-1, 1),
            "rightBot": (1, 1)
        }

        clockwise = {
            "leftTop": "rightTop",
            "rightTop": "rightBot",
            "rightBot": "leftBot",
            "leftBot": "leftTop"
        }

        maxCount = 0
        memo = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    for d in directions:
                        dr, dc = directions[d]
                        maxCount = max(maxCount, 1 + Solution.explore(r + dr, c + dc, grid, 1, d, False, memo, directions, clockwise))
        return maxCount

    def explore(r, c, grid, prev, currentDirection, hasMadeTurn, memo, directions, clockwise):
        if not Solution.inbound(r, c, grid):
            return 0
        key = (r, c, prev, currentDirection, hasMadeTurn)
        if key in memo:
            return memo[key]
        
        if grid[r][c] == 1:
            return 0
        if prev == 1 and grid[r][c] != 2:
            return 0
        if prev == 2 and grid[r][c] != 0:
            return 0
        if prev == 0 and grid[r][c] != 2:
            return 0
        
        maxPath = 0
        dr, dc = directions[currentDirection]

        # go straight
        maxPath = max(maxPath, Solution.explore(r + dr, c + dc, grid, grid[r][c], currentDirection, hasMadeTurn, memo, directions, clockwise))

        # turn
        if not hasMadeTurn:
            newDirection = clockwise[currentDirection]
            dr, dc = directions[newDirection]
            maxPath = max(maxPath, Solution.explore(r + dr, c + dc, grid, grid[r][c], newDirection, True, memo, directions, clockwise))
        
        memo[key] = maxPath + 1
        return memo[key]


    def inbound(r, c, grid):
        rInbound = r >= 0 and r < len(grid)
        cInbound = c >= 0 and c < len(grid[0])
        return rInbound and cInbound