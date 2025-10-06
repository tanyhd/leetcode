import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        return Solution.bfs(grid)

    
    def bfs(grid):
        visited = set()
        priorityQueue = [(grid[0][0], 0,0)]
        maxValue = 0

        while len(priorityQueue) != 0:
            v, r, c = heapq.heappop(priorityQueue)
            visited.add((r,c))
            maxValue = max(maxValue, grid[r][c])

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                break

            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for rD, cD in direction:
                rNew = r + rD
                cNew = c + cD

                if not Solution.inbound(rNew, cNew, grid):
                    continue
                
                if (rNew, cNew) in visited:
                    continue
                
                heapq.heappush(priorityQueue, (grid[rNew][cNew], rNew, cNew))
        
        return maxValue

    def inbound(r, c, grid):
        rInbound = r >= 0 and r < len(grid)
        cInbound = c >= 0 and c < len(grid[0])
        return rInbound and cInbound