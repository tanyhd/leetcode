class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        maxCount = 1
        map = {}
        p1 = 0
        p2 = p1 + 1
        map[fruits[p1]] = 1 

        while p2 < len(fruits):
            f = fruits[p2]
            if f in map:
                map[f] += 1
            else:
                map[f] = 1

            if len(map) <= 2:
                count = 0
                for key in map:
                    count += map[key]
                maxCount = max(maxCount, count)
                p2 += 1
            else:
                f = fruits[p1]
                map[f] -= 1
                if map[f] == 0:
                    del map[f]
                p1 += 1
                p2 += 1

        return maxCount