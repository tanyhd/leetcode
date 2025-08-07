package solution

func numOfUnplacedFruits(fruits []int, baskets []int) int {
	count := len(baskets)
	for i := range fruits {
		for j := range baskets {
			if fruits[i] <= baskets[j] {
				baskets[j] = 0
				count -= 1
				break
			}
		}
	}
	return count
}
