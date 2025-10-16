class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        freq = {}
        for i in range(len(nums)):
            num = nums[i] % value
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        p = 0
        while True:
            num = p % value
            if num not in freq:
                return p
            if freq[num] == 0:
                return p
            freq[num] -= 1
            p+=1
        