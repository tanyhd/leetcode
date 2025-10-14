class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        check = []
        count = []

        p1 = 0
        p2 = p1 + 1

        while p2 < len(nums):
            if nums[p2-1] < nums[p2]:
                p2 += 1
            else:
                count.append((p1, p2-1))
                p1 = p2
                p2 += 1
        count.append((p1, p2-1))
        print(count)
        
        for i in range(len(count)):
            start, end = count[i]
            num = end - start + 1
            if num >= k * 2:
                return True
            
            if i >= len(count) -1:
                break
            startNext, endNext = count[i+1]
            numNext = endNext - startNext + 1
            if num >= k and numNext >= k:
                return True

        return False