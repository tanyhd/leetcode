class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return Solution._flowerGame(n, m, {})
      
    def _flowerGame(n, m, memo):
        if n == 0 or m == 0:
            return 0

        key = (n, m)
        if key in memo:
            return memo[key]
        
        count = 0
        if (n + m) % 2 != 0:
            count += 1

        count += Solution._flowerGame(n-1, m, memo)
        count += Solution._flowerGame(n, m-1, memo)
        count -= Solution._flowerGame(n-1, m-1, memo)

        memo[key] = count
        return count
