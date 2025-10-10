class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        maxEnergy = float('-inf')
        memo = {}
        for i in range(len(energy)):
            maxEnergy = max(maxEnergy, Solution.explore(i, k, energy, memo))
        return maxEnergy

        
    def explore(p, k, energy, memo):
        if p >= len(energy):
            return 0

        if p in memo:
            return memo[p]
        memo[p] = energy[p] + Solution.explore(p+k, k, energy, memo)
        return memo[p]
