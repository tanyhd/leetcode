class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        p1 = 0
        p2 = p1 + 1

        zeroCount = 0
        if nums[p1] == 0:
            zeroCount += 1

        maxCount = 0
        while p2 < len(nums):
            if nums[p2] == 0:
                zeroCount += 1
            
            if zeroCount >= 2:
                while zeroCount >= 2 and p1 <= p2:
                    if nums[p1] == 0:
                        zeroCount -= 1
                        p1 += 1
                        break
                    p1 += 1
                
            maxCount = max(maxCount, p2-p1)
            p2 += 1

        
        return maxCount