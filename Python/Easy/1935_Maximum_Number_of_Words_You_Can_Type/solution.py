class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        textArray = text.split()
        letterSet = set()
        
        for letter in brokenLetters:
            letterSet.add(letter)

        count = 0
        for t in textArray:
            for w in t:
                if w in letterSet:
                    count -= 1
                    break
            count += 1
        return count
            