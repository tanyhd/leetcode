class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        stack = []
        for i in range(len(nums)):
            current = nums[i]
            while len(stack) != 0 and not Solution.isCoprime(stack[-1], current):
                num = stack.pop()
                current = Solution.LCM(num, current)
            stack.append(current)
        
        return stack
 

    def isCoprime(a, b):
        return Solution.gcd(a, b) == 1

    def LCM(a, b):
        g = Solution.gcd(a, b)
        return a // g * b

    def gcd(a, b):
        while b != 0:
            a, b = b, a%b
        return a