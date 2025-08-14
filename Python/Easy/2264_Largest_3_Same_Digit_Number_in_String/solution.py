class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxNum = -1

        for i in range(1, len(num) - 1):
            if num[i-1] == num[i] and num[i] == num[i+1]:
                maxNum = max(maxNum, int(num[i]))

        if maxNum == -1:
            return ""
        return str(maxNum) * 3 