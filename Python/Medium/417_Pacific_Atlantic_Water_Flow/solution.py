class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        output = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                PO, AO = Solution.explore(r, c, heights, float("inf"), set())
                if PO and AO:
                    output.append([r,c])
        return output
                    
    def explore(r, c, height, pHeight, visited):
        if r < 0 or c < 0:
            return (True, False)
        if r >= len(height) or c >= len(height[0]):
            return (False, True)

        cHeight = height[r][c]
        if pHeight < cHeight:
            return (False, False)
        
        if (r, c) in visited:
            return (False, False)
        visited.add((r,c))

        upPO, upAO = Solution.explore(r-1, c, height, cHeight, visited)
        downPO, downAO = Solution.explore(r+1, c, height, cHeight, visited)
        leftPO, leftAO = Solution.explore(r, c-1, height, cHeight, visited)
        rightPO, rightAO = Solution.explore(r, c+1, height, cHeight, visited)
        return ((upPO or downPO or leftPO or rightPO), (upAO or downAO or leftAO or rightAO))

   