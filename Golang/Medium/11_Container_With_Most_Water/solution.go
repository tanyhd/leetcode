package containerwithmostwater

func maxArea(height []int) int {
	maxArea := 0
	p1 := 0
	p2 := len(height) - 1

	for p1 < p2 {
		area := (p2 - p1) * min(height[p2], height[p1])
		maxArea = max(maxArea, area)
		if height[p2] < height[p1] {
			p2 -= 1
		} else {
			p1 += 1
		}
	}
	return maxArea
}
