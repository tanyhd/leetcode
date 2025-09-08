class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1, n + 1):
            if Solution.checkZero(i) and Solution.checkZero(n-i):
                return [i, n-i]

    def checkZero(num):
        while num > 9:
            if num % 10 == 0:
                return False
            num //= 10
        return True