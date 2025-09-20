from collections import deque
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.packetSet = set()
        self.destinationTimeMap = {}
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        item = (source, destination, timestamp)
        if item in self.packetSet:
            return False
        
        self.packetSet.add(item)
        self.queue.append(item)
        if len(self.queue) > self.limit:
            oldItem = self.queue.popleft()
            self.packetSet.remove(oldItem)

            _, oldDestination, oldTime = oldItem
            self.destinationTimeMap[oldDestination].remove(oldTime)
        
        if destination not in self.destinationTimeMap:
            self.destinationTimeMap[destination] = []
        self.destinationTimeMap[destination].append(timestamp)

        return True

    def forwardPacket(self) -> list[int]:
        if len(self.queue) == 0:
            return []
        
        source, destination, timestamp = self.queue.popleft()
        self.packetSet.remove((source, destination, timestamp))
        self.destinationTimeMap[destination].remove(timestamp)
        return [source, destination, timestamp]
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destinationTimeMap:
            return 0
        
        timeArray = self.destinationTimeMap[destination]

        start = bisect_left(timeArray, startTime)
        end = bisect_right(timeArray, endTime)
        return end - start


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)