package minimumoperationstomakearraysumdivisiblebyk

func minOperations(nums []int, k int) int {
	sumNum := 0
	for _, num := range nums {
		sumNum += num
	}

	count := 0
	for sumNum%k != 0 {
		count += 1
		sumNum -= 1
	}
	return count
}
