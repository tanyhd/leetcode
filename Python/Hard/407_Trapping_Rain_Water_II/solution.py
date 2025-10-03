import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        heightMinHeap = []
        visited = set()

        for r in range(len(heightMap)):
            for c in range(len(heightMap[0])):
                if r == 0 or c == 0 or r == len(heightMap) - 1 or c == len(heightMap[0]) - 1:
                    heapq.heappush(heightMinHeap, (heightMap[r][c], r, c))
                    visited.add((r,c))
        
        waterLevel = 0
        trapWater = 0

        while len(heightMinHeap) != 0:
            level, r, c = heapq.heappop(heightMinHeap)
            waterLevel = max(waterLevel, level)

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                rNew = r + dr
                cNew = c + dc
                if Solution.inbound(rNew, cNew, heightMap) and (rNew, cNew) not in visited:
                    visited.add((rNew, cNew))
                    heapq.heappush(heightMinHeap, (heightMap[rNew][cNew], rNew, cNew))
                    newLevel = heightMap[rNew][cNew]
                    if newLevel < waterLevel:
                        trapWater += waterLevel - newLevel

        return trapWater
        
    def inbound(r, c, grid):
        rInbound = r >= 0 and r < len(grid)
        cInbound = c >= 0 and c < len(grid[0])
        return rInbound and cInbound
