class Solution:
    def maxDistinctElements(self, nums: list[int], k: int) -> int:
        nums.sort()
        prev = float("-inf")
        count = 0

        for i in range(len(nums)):
            current = min(max(nums[i] - k, prev + 1), nums[i] + k)
            if current > prev:
                count += 1
                prev = current 

        return count