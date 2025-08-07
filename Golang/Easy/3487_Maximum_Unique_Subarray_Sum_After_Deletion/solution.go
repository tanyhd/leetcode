package maximumuniquesubarraysumafterdeletion

func maxSum(nums []int) int {
	maxSum := 0
	mapSet := make(map[int]bool)

	for _, num := range nums {
		if _, exist := mapSet[num]; !exist {
			mapSet[num] = true
			if num > 0 {
				maxSum += num
			}
		}
	}
	if maxSum == 0 {
		first := true
		for key, _ := range mapSet {
			if first {
				maxSum = key
				first = false
				continue
			}
			maxSum = max(maxSum, key)
		}
		return maxSum
	}
	return maxSum
}
