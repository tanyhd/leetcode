from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        output = []
        p1 = 0
        p2 = k - 1

        while p2 < len(nums):
            output.append(Solution.calculateSum(p1, p2, nums, x))
            p1 += 1
            p2 += 1
        return output
    

    def calculateSum(p1, p2, nums, x):
        numMap = {}
        for i in range(p1, p2+1):
            if nums[i] not in numMap:
                numMap[nums[i]] = 0
            numMap[nums[i]] += 1
        
        numArray = []
        for num in numMap:
            numArray.append((numMap[num], num))
        
        numArray.sort(reverse=True)
        total = 0
        length = min(len(numArray), x)
        for i in range(length):
            count, num = numArray[i]
            total += num * count
        return total