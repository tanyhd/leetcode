class Solution:
    def hasSameDigits(self, s: str) -> bool:
        current = s

        while len(current) > 2:
            temp = ""
            for i in range(len(current)-1):
                temp += str((int(current[i]) + int(current[i+1])) % 10)
            current = temp

        return current[0] == current[1]