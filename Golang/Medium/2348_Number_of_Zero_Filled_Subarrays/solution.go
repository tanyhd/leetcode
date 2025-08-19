package numberofzerofilledsubarrays

func zeroFilledSubarray(nums []int) int64 {
	count := 0
	totalCount := int64(0)

	for _, num := range nums {
		if num == 0 {
			count += 1
			totalCount += int64(count)
		} else {
			count = 0
		}
	}
	return totalCount
}
