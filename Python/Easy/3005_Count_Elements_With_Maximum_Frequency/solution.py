class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        maxCount = 0
        countMap = {}

        for num in nums:
            if num not in countMap:
                countMap[num] = 0
            countMap[num] += 1
            maxCount = max(maxCount, countMap[num])

        count = 0
        for num in countMap:
            if countMap[num] == maxCount:
                count += countMap[num]
        return count