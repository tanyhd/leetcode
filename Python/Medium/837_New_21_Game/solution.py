class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        return Solution._new21Game(n, 0, k, maxPts, {})

    def _new21Game(n, total, k, maxPts, memo):
        key = total
        if key in memo:
            return memo[key]

        if total >= k:
            if total <= n:
                return 1.0
            else:
                return 0.0
        
        count = 0
        for i in range(1, maxPts+1):
            count += Solution._new21Game(n, total + i, k, maxPts, memo)/ maxPts
        memo[key] = count
        return count