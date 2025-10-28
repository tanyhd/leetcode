class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            right = Solution.simulateMovement(i, nums.copy(), 1)
            if Solution.isAllZero(right):
                count += 1

            left = Solution.simulateMovement(i, nums.copy(), -1)
            if Solution.isAllZero(left):
                count += 1
        return count

    def simulateMovement(p, array, sign):
        while p < len(array) and p >= 0:
            if array[p] == 0:
                p += sign
                continue
            else:
                array[p] -= 1
            sign *= -1
            p += sign
        return array

    def isAllZero(nums):
        for i in range(len(nums)):
            if nums[i] != 0:
                return False
        return True