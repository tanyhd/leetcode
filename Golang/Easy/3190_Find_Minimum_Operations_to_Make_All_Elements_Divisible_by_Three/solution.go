package findminimumoperationstomakeallelementsdivisiblebythree

func minimumOperations(nums []int) int {
	count := 0
	for _, num := range nums {
		if num%3 != 0 {
			count += 1
		}
	}
	return count
}
