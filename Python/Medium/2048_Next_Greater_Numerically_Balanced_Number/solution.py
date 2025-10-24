class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n+=1
        while not Solution.isNumBalance(n):
            n += 1
        return n

    def isNumBalance(n):
        numMap = {}
        while n > 0:
            r = n % 10
            if r not in numMap:
                numMap[r] = 0
            numMap[r] += 1
            n = n//10

        for num in numMap:
            if numMap[num] != num:
                return False
        return True