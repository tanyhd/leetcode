class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        numMap = {}
        output = []

        for num in nums:
            if num in numMap:
                output.append(num)
            else:
                numMap[num] = 1
        return output