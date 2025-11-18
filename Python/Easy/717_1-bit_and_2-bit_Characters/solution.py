from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        return Solution.helper(0, bits)
    
    def helper(p, bits):
        if p >= len(bits):
            return False
        if p == len(bits) - 1:
            return True
        
        one = two = False
        if bits[p] == 0:
            one = Solution.helper(p+1, bits)
        elif bits[p] == 1:
            two = Solution.helper(p+2, bits)
        return one or two