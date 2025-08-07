class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        count = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    baskets[j] = 0
                    count += 1
                    break

        return len(fruits) - count