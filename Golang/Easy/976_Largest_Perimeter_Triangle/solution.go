package largestperimetertriangle

import "sort"

func largestPerimeter(nums []int) int {
	sort.Ints(nums)

	for i := len(nums) - 1; i > 1; i-- {
		a := nums[i]
		b := nums[i-1]
		c := nums[i-2]

		if a+b > c && a+c > b && b+c > a {
			return a + b + c
		}
	}
	return 0
}
