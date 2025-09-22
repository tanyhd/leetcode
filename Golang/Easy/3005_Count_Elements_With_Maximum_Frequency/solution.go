package countelementswithmaximumfrequency

func maxFrequencyElements(nums []int) int {
	maxCount := 0
	countMap := make(map[int]int)

	for _, num := range nums {
		countMap[num] += 1
		maxCount = max(maxCount, countMap[num])
	}

	count := 0
	for num, _ := range countMap {
		if countMap[num] == maxCount {
			count += countMap[num]
		}
	}
	return count
}
