from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        return Solution.helper(nums, 0, 0, {})

    def helper(nums, p, rem, memo):
        key = (p, rem)
        if key in memo:
            return memo[key]

        if p == len(nums):
            if rem == 0:
                return 0
            return float('-inf')
        
        pick = nums[p] + Solution.helper(nums, p+1,(rem + nums[p]) % 3, memo)
        dunPick = Solution.helper(nums, p+1, rem, memo)

        memo[key] = max(pick, dunPick)
        return memo[key]