class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        return Solution.person(1, 1, n, delay, forget, {})
        
    def person(start, currentDay, n, delay, forget, memo):
        MOD = 10**9 + 7
        
        key = (start, currentDay)
        if key in memo:
            return memo[key]

        if currentDay > n:
            if n - start < forget:
                return 1
            else:
                return 0 

        count = 0
        if start + delay <= currentDay and currentDay - start < forget:
            count += Solution.person(currentDay, currentDay + 1, n, delay, forget, memo) % MOD

        count += Solution.person(start, currentDay + 1, n, delay, forget, memo) % MOD
        
        memo[key] = count
        return count