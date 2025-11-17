package checkifall1areatleastlengthkplacesaway

func kLengthApart(nums []int, k int) bool {
	count := 0
	hasStarted := false

	for i, _ := range nums {
		if nums[i] == 0 {
			count += 1
		} else {
			if count < k && hasStarted {
				return false
			}
			hasStarted = true
			count = 0
		}
	}
	return true
}
