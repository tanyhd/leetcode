class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        count = target[0]

        for i in range(0, len(target)-1):
            if target[i] < target[i+1]:
                count += target[i+1] - target[i]
        return count