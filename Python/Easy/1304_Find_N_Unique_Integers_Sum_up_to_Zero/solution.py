class Solution:
    def sumZero(self, n: int) -> list[int]:
        output = []
        count = 0
        for i in range(1, n+1):
            if i == n:
                output.append(count*-1)
            else:
                output.append(i)
                count += i
        return output