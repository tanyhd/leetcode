class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(61):
            target = num1 - (k * num2)
            if target < 0:
                continue

            if bin(target).count("1") <= k <= target:
                return k

        return -1
    

#TLE brute force
''' 
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ops = Solution._helper(num1, num2, 0, {})
        if ops == float("inf"):
            return -1
        return ops


    def _helper(num1, num2, k, memo):
        if num1 < 0:
            return float("inf")
        if num1 == 0:
            return k
        if k > 60:
            return float("inf")
        key = (num1, k)
        if key in memo:
            return memo[key]
        
        count = float("inf")
        for i in range(61):
            newNum = num1 - (2**i + num2)
            count = min(count, Solution._helper(newNum, num2, k+1, memo))
        
        memo[key] = count
        return count
'''