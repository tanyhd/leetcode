class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles

        while numBottles >= numExchange:
            rem = numBottles % numExchange
            numBottles = numBottles // numExchange
            count += numBottles
            numBottles += rem
        return count
