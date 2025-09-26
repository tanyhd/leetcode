package validtrianglenumber

import "sort"

func triangleNumber(nums []int) int {
	count := 0
	sort.Ints(nums)

	for i, _ := range nums {
		a := nums[i]
		pB := 0
		pC := i - 1

		for pB < pC {
			b := nums[pB]
			c := nums[pC]

			if a+b > c && a+c > b && b+c > a {
				count += pC - pB
				pC -= 1
			} else {
				pB += 1
			}
		}
	}
	return count
}
