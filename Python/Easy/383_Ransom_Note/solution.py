class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for c in magazine:
            if c not in map:
                map[c] = 0
            map[c] += 1

        for c in ransomNote:
            if c not in map:
                return False
            map[c] -= 1
            if map[c] < 0:
                return False
        return True