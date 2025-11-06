import heapq
from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        stationMap = {}
        stationStatus = set()

        for i in range(1, c+1):
            stationMap[i] = []
            stationStatus.add((i, True))

        for connection in connections:
            a, b = connection[0], connection[1]
            stationMap[a].append(b)
            stationMap[b].append(a)
        
        visited = set()
        connectedStation = {}
        connectedCountMap = {}

        connectedCount = 1
        for i in range(1, c+1):
            if i in visited:
                continue
            
            stack = [i]
            while len(stack) != 0:
                current = stack.pop()
                connectedStation[current] = connectedCount
                if connectedCount not in connectedCountMap:
                    connectedCountMap[connectedCount] = []
                connectedCountMap[connectedCount].append(current)

                for neighbour in stationMap[current]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        stack.append(neighbour)
            
            connectedCount += 1
        
        for connection in connectedCountMap:
            heapq.heapify(connectedCountMap[connection])
            
        output = []
        for query in queries:
            state, station = query[0], query[1]
            if state == 1:
                if (station, True) in stationStatus:
                    output.append(station)
                else:
                    h = connectedCountMap[connectedStation[station]]
                    while h and (h[0], True) not in stationStatus:
                        heapq.heappop(h)

                    if len(h) != 0:
                        output.append(h[0])
                    else:
                        output.append(-1) 
                    
            if state == 2:
                if (station, True) in stationStatus:
                    stationStatus.remove((station, True))
                stationStatus.add((station, False))
        return output