from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 0
            numMap[num] += 1
        
        while original in numMap:
            original = original * 2
        
        return original