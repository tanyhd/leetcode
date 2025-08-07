class Solution:
    def maxSum(self, nums: list[int]) -> int:
        maxSum = 0
        map = {}
        for num in nums:
            if num not in map:
                map[num] = True
                if num > 0:
                    maxSum += num
        
        if maxSum == 0:
            return max(map)
        return maxSum