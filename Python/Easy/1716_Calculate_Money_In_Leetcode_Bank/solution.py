class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        count = 0

        for i in range(1, n+1):
            count += start
            start += 1

            if i % 7 == 0:
                start = start - 7 + 1

        return count