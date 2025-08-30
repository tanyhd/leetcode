import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        maxD = 0
        maxArea = 0

        for d in range(len(dimensions)):
            l, b = dimensions[d]
            currentD = math.sqrt(l*l + b*b)
            if currentD > maxD:
                maxD = currentD
                maxArea = l*b
            elif currentD == maxD:
                maxArea = max(maxArea, l*b)
        return maxArea