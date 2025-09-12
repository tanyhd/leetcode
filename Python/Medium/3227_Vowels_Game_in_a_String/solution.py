class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {"a": True, "e":True, "i":True, "o":True, "u":True}

        for c in s:
            if c in vowels:
                return True
        return False
