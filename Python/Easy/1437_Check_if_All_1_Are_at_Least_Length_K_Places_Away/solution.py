from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        hasStarted = False
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                if count < k and hasStarted:
                    return False
                hasStarted = True
                count = 0
        return True