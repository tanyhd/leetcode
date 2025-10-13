class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        output = [words[0]]

        for i in range(1, len(words)):
            if Solution.isAnagram(output[-1], words[i]):
                continue
            output.append(words[i])
        
        return output


    def isAnagram(s1, s2):
        if len(s1) != len(s2):
            return False
        
        s1Map = {}
        for w in s1:
            if w not in s1Map:
                s1Map[w] = 0
            s1Map[w] += 1
        
        for w in s2:
            if w not in s1Map:
                return False
            s1Map[w] -= 1
            if s1Map[w] == 0:
                del s1Map[w]

        return len(s1Map) == 0  