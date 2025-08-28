class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        output = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 or c == 0:
                    ls = []
                    Solution.explore(r, c, grid, ls)
                    if r == 0 and c == 0:
                        ls.sort(reverse=True)
                    elif r == 0:
                        ls.sort()
                    else:
                        ls.sort(reverse=True)

                    Solution.exploreUpdate(r, c, grid, ls, 0)
        return grid

    def explore(r, c, grid, ls):
        if not Solution.inbound(r, c, grid):
            return
        ls.append(grid[r][c])
        Solution.explore(r+1, c+1, grid, ls)

    def exploreUpdate(r, c, grid, updateLst, pos):
        if not Solution.inbound(r, c, grid):
            return
        grid[r][c] = updateLst[pos]
        Solution.exploreUpdate(r+1, c+1, grid, updateLst, pos+1)

    def inbound(r, c, grid):
        rInbound = r >= 0 and r < len(grid)
        cInbound = c >= 0 and c < len(grid[0])
        return rInbound and cInbound