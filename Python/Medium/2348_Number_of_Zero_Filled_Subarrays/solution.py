class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0
        totalCount = 0

        for num in nums:
            if num == 0:
                count += 1
                totalCount += count
            else:
                count = 0
        return totalCount