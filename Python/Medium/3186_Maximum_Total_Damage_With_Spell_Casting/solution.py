import bisect

class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        return Solution.helper(0, power, {})
    

    def helper(p, power, memo):
        if p >= len(power):
            return 0
        
        if p in memo:
            return memo[p]
        
        current = power[p]

        j = bisect.bisect_right(power, current)
        k = bisect.bisect_right(power, current + 2)

        count = j - p
            
        used = (current * count) + Solution.helper(k, power, memo)
        notUsed = Solution.helper(j, power, memo)

        memo[p] = max(used, notUsed)
        return memo[p]