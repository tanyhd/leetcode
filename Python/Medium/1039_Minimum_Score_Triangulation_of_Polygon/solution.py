class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        return Solution.helper(values, 0, len(values)-1, {})
    
    def helper(v, i, j, memo):
        if j - i < 2:
            return 0

        key = (i, j)
        if key in memo:
            return memo[key]

        minScore = float("inf")
        for k in range(i + 1, j):
            score = (v[i] * v[j] * v[k]) + Solution.helper(v, i, k, memo) + Solution.helper(v, k, j, memo)
            minScore = min(minScore, score)
        
        memo[key] = minScore
        return minScore