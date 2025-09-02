class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        pointsMap = {}
        for i in range(len(points)):
            x, y = points[i]
            pointsMap[(x,y)] = True

        count = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]

                if xi <= xj and yi >= yj:
                    if Solution.check(points[i], points[j], pointsMap):
                        count += 1
                elif xi >= xj and yi <= yj:
                    if Solution.check(points[j], points[i], pointsMap):
                        count += 1
             
        return count

    def check(a, b, pointsMap):
        xi, yi = a
        xj, yj = b
        rangeX = xj-xi
        rangeY = yi-yj

        for i in range(0, 1 + rangeX):
            for j in range(0, 1 + rangeY):
                checkX = xi + i
                checkY = yi - j
                if (checkX == xi and checkY == yi) or (checkX == xj and checkY == yj):
                    continue
                if (checkX, checkY) in pointsMap:
                    return False
               
        return True
