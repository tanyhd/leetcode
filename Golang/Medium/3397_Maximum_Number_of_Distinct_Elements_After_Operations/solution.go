package maximumnumberofdistinctelementsafteroperations

import (
	"math"
	"sort"
)

func maxDistinctElements(nums []int, k int) int {
	sort.Ints(nums)
	prev := math.MinInt
	count := 0

	for _, num := range nums {
		current := min(max(num-k, prev+1), num+k)
		if current > prev {
			count += 1
			prev = current
		}
	}
	return count
}
