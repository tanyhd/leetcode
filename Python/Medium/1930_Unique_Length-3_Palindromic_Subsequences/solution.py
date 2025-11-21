class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letterSet = set()
        letterMap = {}

        for i in range(len(s)):
            c = s[i]
            if c not in letterSet:
                letterSet.add(c)
                letterMap[c] = [i]
            else:
                letterMap[c].append(i)
        
        count = 0
        for c in letterSet:
            startIndex = letterMap[c][0]
            endIndex = letterMap[c][-1]

            betweenSet = set()
            for i in range(startIndex + 1, endIndex):
                betweenSet.add(s[i])
            
            count += len(betweenSet)
        return count
            
