class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        count = 0
        nums.sort()

        for i in range(len(nums)-1, 1, -1):
            a = nums[i]
            pB = 0
            pC = i-1

            while pB < pC:
                b = nums[pB]
                c = nums[pC]

                if a + b > c and a + c > b and b + c > a:
                    count += pC - pB
                    pC -= 1
                else:
                    pB += 1
            
        return count