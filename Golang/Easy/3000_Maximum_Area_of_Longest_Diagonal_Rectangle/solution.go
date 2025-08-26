package maximumareaoflongestdiagonalrectangle

import "math"

func areaOfMaxDiagonal(dimensions [][]int) int {
	maxD := float64(0)
	maxArea := 0

	for i := range dimensions {
		l := dimensions[i][0]
		b := dimensions[i][1]
		currentD := math.Sqrt(float64(l*l + b*b))
		if currentD > maxD {
			maxD = currentD
			maxArea = l * b
		} else if currentD == maxD {
			maxArea = max(maxArea, l*b)
		}
	}
	return maxArea
}
