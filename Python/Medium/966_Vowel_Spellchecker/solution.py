class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        output = []
        exactMap = {}
        lowerMap = {}
        vowelMap = {}

        for w in wordlist:
            exactMap[w] = [w]

            if w.lower() not in lowerMap:
                lowerMap[w.lower()] = []
            lowerMap[w.lower()].append(w)

            wordConvert = Solution.convertVowelWord(w.lower())
            if wordConvert not in vowelMap:
                vowelMap[wordConvert] = []
            vowelMap[wordConvert].append(w)

        for q in queries:
            if q in exactMap:
                output.append(exactMap[q][0])
            elif q.lower() in lowerMap:
                output.append(lowerMap[q.lower()][0])
            elif Solution.convertVowelWord(q.lower()) in vowelMap:
                convertWord = Solution.convertVowelWord(q.lower())
                output.append(vowelMap[convertWord][0])
            else:
                output.append("")
        return output


    def convertVowelWord(w):
        vowels = ["a", "e", "i", "o", "u"]
        output = ""
        for c in w:
            if c in vowels:
                output+="*"
            else:
                output+=c
       
        return output
