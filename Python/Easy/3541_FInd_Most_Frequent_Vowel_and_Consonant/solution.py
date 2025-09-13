class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        cMap = {}
        maxVowel = 0
        maxConsonant = 0

        for c in s:
            if c in vowels:
                if c not in cMap:
                    cMap[c] = 0
                cMap[c] += 1
                maxVowel = max(maxVowel, cMap[c])
            else:
                if c not in cMap:
                    cMap[c] = 0
                cMap[c] += 1
                maxConsonant = max(maxConsonant, cMap[c])
        
        return maxVowel + maxConsonant

