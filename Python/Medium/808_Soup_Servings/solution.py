class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        return Solution._soupServings(n, n, {})

    def _soupServings(a, b, memo):
        if (a,b) in memo:
            return memo[(a,b)]
        if a <= 0 and b > 0:
            return 1
        if a <= 0 and b <= 0:
            return 0.5
        if a > 0 and b <= 0:
            return 0

        count = 0
        count += Solution._soupServings(a-100, b, memo)
        count += Solution._soupServings(a-75, b-25, memo)
        count += Solution._soupServings(a-50, b-50, memo)
        count += Solution._soupServings(a-25, b-75, memo)
        memo[(a,b)] = count * 0.25
        return memo[(a,b)]