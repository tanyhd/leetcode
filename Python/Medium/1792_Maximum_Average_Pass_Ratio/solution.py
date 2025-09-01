import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        classArrange = []
        for students in classes:
            passNum, total = students
            potentialIncrease = ((passNum + 1) / (total + 1)) - passNum/total
            heapq.heappush(classArrange, (-1 * potentialIncrease, passNum, total))

        for i in range(1, extraStudents + 1):
            _, passNum, total = heapq.heappop(classArrange)
            passNum += 1
            total += 1
            potentialIncrease = ((passNum + 1) / (total + 1)) - passNum/total
            heapq.heappush(classArrange, (-1 * potentialIncrease, passNum, total))

        count = 0
        for i in range(len(classArrange)):
            _, passNum, total = classArrange[i]
            count += passNum/total 
        return count/len(classArrange)