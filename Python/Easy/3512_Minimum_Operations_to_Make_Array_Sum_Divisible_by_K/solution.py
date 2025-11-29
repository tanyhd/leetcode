from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sumNum = 0
        for num in nums:
            sumNum += num
        
        count = 0
        while sumNum % k != 0:
            count += 1
            sumNum -= 1

        return count