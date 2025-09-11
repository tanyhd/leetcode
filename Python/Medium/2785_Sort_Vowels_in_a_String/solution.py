class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        sorting = []
        for w in s:
            if w in vowels:
              sorting.append(w)
        
        sorting.sort(reverse=True)
        output = ""
        for w in s:
            if w in vowels:
                output += sorting.pop()
            else:
                output += w
        return output
