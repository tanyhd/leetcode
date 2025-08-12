class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        powers = []
        for i in range(1, n+1):
            if i**x <= n:
                powers.append(i**x)
        MOD = 10**9 + 7
        return Solution._numberOfWays(n, x, powers, 0, {}) % MOD


    def _numberOfWays(n, x, powers, pos, memo):
        key = (n, pos)
        if key in memo:
            return memo[key]
        if n == 0:
            return 1
        if n < 0:
            return 0
        if pos >= len(powers):
            return 0
        
        num = powers[pos]
        count = 0
        count += Solution._numberOfWays(n, x, powers, pos+1, memo)
        count += Solution._numberOfWays(n-num, x, powers, pos+1, memo)
        memo[key] = count
        return count