class Solution:
    def triangularSum(self, nums: list[int]) -> int:

        while len(nums) > 1:
            tempArray = []
            for i in range(len(nums)-1):
                tempArray.append((nums[i] + nums[i+1]) % 10)
            
            nums = tempArray
        
        return nums[0]