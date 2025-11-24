from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        numBin = ""
        output = []
        for num in nums:
            numBin += str(num)
            decNum = int(numBin, 2)
            if decNum % 5 == 0:
                output.append(True)
            else:
                output.append(False)
        return output