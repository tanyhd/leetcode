package smallestnumberwithallsetbits

import "math"

func smallestNumber(n int) int {
	binLength := 0
	for n != 0 {
		binLength += 1
		n = n / 2
	}

	count := 0
	for i := range binLength {
		count += int(math.Pow(2, float64(i)))
	}
	return count
}
