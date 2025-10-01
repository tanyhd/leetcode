package waterbottles

func numWaterBottles(numBottles int, numExchange int) int {
	count := numBottles

	for numBottles >= numExchange {
		rem := numBottles % numExchange
		numBottles = numBottles / numExchange
		count += numBottles
		numBottles += rem
	}
	return count
}
