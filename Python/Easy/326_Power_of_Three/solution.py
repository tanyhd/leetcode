class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        for i in range (n):
            if 3**i > n:
                break
            if 3**i == n:
                return True
        return False