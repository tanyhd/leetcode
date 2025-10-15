package adjacentincreasingsubarraysdetectionii

func maxIncreasingSubarrays(nums []int) int {
	count := [][]int{}

	p1 := 0
	p2 := p1 + 1

	for p2 < len(nums) {
		if nums[p2-1] < nums[p2] {
			p2 += 1
		} else {
			count = append(count, []int{p1, p2 - 1})
			p1 = p2
			p2 += 1
		}
	}
	count = append(count, []int{p1, p2 - 1})

	maxCount := 0
	for i, _ := range count {
		start, stop := count[i][0], count[i][1]
		current := stop - start + 1
		maxCount = max(maxCount, current/2)

		if i >= len(count)-1 {
			break
		}
		startNext, stopNext := count[i+1][0], count[i+1][1]
		nextValue := stopNext - startNext + 1
		maxCount = max(maxCount, min(current, nextValue))
	}
	return maxCount
}
