from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        wallSet = set()
        for wall in walls:
            wallSet.add((wall[0], wall[1]))
        
        guardSet = set()
        for guard in guards:
            guardSet.add((guard[0], guard[1]))
        
        seen = set()

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for guard in guards:
            for dir in direction:
                dr, dc = dir
                Solution.guardExplore(guard[0], guard[1], dr, dc, m, n, wallSet, guardSet, seen)
        
        return m*n - len(seen) - len(wallSet) - len(guardSet)

    

    def guardExplore(r, c, dr, dc, m, n, wallSet, guardSet, seen):
        r += dr
        c += dc

        if not Solution.inbound(r, c, m, n):
            return
        
        if (r, c) in wallSet or (r, c) in guardSet:
            return
        
        seen.add((r,c))
        Solution.guardExplore(r, c, dr, dc, m, n, wallSet, guardSet, seen)


    def inbound(r, c, m, n):
        rInbound = r >= 0 and r < m
        cInbound = c >= 0 and c < n
        return rInbound and cInbound