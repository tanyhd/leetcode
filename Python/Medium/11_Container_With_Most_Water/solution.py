class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = 0
        p1 = 0
        p2 = len(height) - 1

        while p1 < p2:
            area = (p2 - p1) * min(height[p1], height[p2])
            maxArea = max(maxArea, area)
            if height[p2] < height[p1]:
                p2 -= 1
            else:
                p1 += 1
        return maxArea