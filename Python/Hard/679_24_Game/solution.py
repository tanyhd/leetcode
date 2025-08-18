class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        return Solution._judgePoint24(cards)

    def _judgePoint24(nums):
        if len(nums) == 1:
            if nums[0] == 24 or abs(nums[0] - 24) < 0.01:
                return True
            return False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a, b = nums[i], nums[j]

                rest = []
                for n in range(len(nums)):
                    if n != i and n != j:
                        rest.append(nums[n])

                combination = [a+b, a-b, b-a, a*b]
                if abs(a) > 1e-6:
                    combination.append(b/a)
                if abs(b) > 1e-6:
                    combination.append(a/b)

                for val in combination:
                    if Solution._judgePoint24([val]+rest) == True:
                        return True
      
        return False

