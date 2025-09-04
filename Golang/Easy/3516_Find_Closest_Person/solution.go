package findclosestperson

import "math"

func findClosest(x int, y int, z int) int {
	a := math.Abs(float64(x - z))
	b := math.Abs(float64(y - z))

	if a == b {
		return 0
	}

	if a < b {
		return 1
	}

	return 2
}
