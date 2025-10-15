class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        check = []
        count = []

        p1 = 0
        p2 = p1 + 1

        while p2 < len(nums):
            if nums[p2-1] < nums[p2]:
                p2 += 1
            else:
                count.append((p1, p2-1))
                p1 = p2
                p2 += 1
        count.append((p1, p2-1))

        maxCount = 0
        for i in range(len(count)):
            start, stop = count[i]
            current = stop - start + 1
            maxCount = max(maxCount, current//2)

            if i >= len(count) - 1:
                break
            startNext, stopNext = count[i+1]
            nextValue = stopNext - startNext + 1
            maxCount = max(maxCount, min(current, nextValue))
        
        return maxCount
