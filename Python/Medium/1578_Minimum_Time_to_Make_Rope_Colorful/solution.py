from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        count = 0

        p1 = 0 
        p2 = p1 + 1

        while p2 < len(colors):
            if colors[p1] == colors[p2]:
                count += min(neededTime[p1], neededTime[p2])
                if neededTime[p2] < neededTime[p1]:
                    neededTime[p2] = neededTime[p1]
            
            p1 += 1
            p2 += 1
        
        return count
