from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return Solution._helper(strs, 0, m, n, {})

    
    def _helper(s, p, m, n, memo):
        key = (p, m, n)
        if key in memo:
            return memo[key]

        if p >= len(s):
            return 0
        
        currentS = s[p]
        mCount = 0
        nCount = 0
        for c in currentS:
            if c == "1":
                nCount += 1
            if c == "0":
                mCount += 1

        include = 0
        if mCount <= m and nCount <= n:
            include = Solution._helper(s, p+1, m - mCount, n - nCount, memo) + 1

        exclude = Solution._helper(s, p+1, m, n, memo)

        memo[key] = max(include, exclude)
        return memo[key]