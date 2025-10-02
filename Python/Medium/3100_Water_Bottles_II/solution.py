class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = 0
        full = numBottles
        empty = 0
        
        while full != 0:
            drunk += full
            empty += full
            full = 0

            if empty > 0 and empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                full += 1
        return drunk 
