package powerofthree

import "math"

func isPowerOfThree(n int) bool {
	if n == 0 {
		return false
	}

	for i := range n {
		num := int(math.Pow(float64(3), float64(i)))
		if num > n {
			return false
		}
		if num == n {
			return true
		}
	}
	return false
}
