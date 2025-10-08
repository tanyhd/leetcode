class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        output = []
        potions.sort()

        for i in range(len(spells)):
            count = 0

            p1 = 0
            p2 = len(potions) - 1

            while p1 <= p2:
                mid = (p2 + p1) // 2
                power = spells[i] * potions[mid]
                if power < success:
                    p1 = mid + 1
                else:
                    p2 = mid - 1
            
            count += len(potions) - p1
            output.append(count)
        return output        