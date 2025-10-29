class Solution:
    def smallestNumber(self, n: int) -> int:
        binLength = 0
        while n != 0:
            binLength += 1
            n = n // 2
        
        count = 0
        for i in range(binLength):
            count += (2 ** i)
        
        return count