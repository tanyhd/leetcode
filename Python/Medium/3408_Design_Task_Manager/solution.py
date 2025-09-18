import heapq

class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.usersTask = []
        self.TaskToUser = {}

        for task in tasks:
            userId, taskId, priority = task
            heapq.heappush(self.usersTask, (-priority, -taskId))
            self.TaskToUser[taskId] = (userId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.usersTask, (-priority, -taskId))
        self.TaskToUser[taskId] = (userId, priority)

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.usersTask, (-newPriority, -taskId))
        userId, _ = self.TaskToUser[taskId]
        self.TaskToUser[taskId] = (userId, newPriority)
        
    def rmv(self, taskId: int) -> None:
        del self.TaskToUser[taskId]

    def execTop(self) -> int:
        while len(self.usersTask) != 0:
            priority, topTaskId = self.usersTask[0]
            topTaskId = -1 * topTaskId

            if topTaskId not in self.TaskToUser:
                heapq.heappop(self.usersTask)
                continue
            
            _, actualPriority = self.TaskToUser[topTaskId]
            if -1 * priority == actualPriority:
                heapq.heappop(self.usersTask)
                userId, _ = self.TaskToUser[topTaskId]
                del self.TaskToUser[topTaskId]
                return userId
                
            heapq.heappop(self.usersTask)
            
        return -1
        
# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()