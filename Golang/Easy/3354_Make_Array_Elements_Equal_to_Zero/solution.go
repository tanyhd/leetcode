package makearrayelementsequaltozero

func countValidSelections(nums []int) int {
	count := 0
	for i, _ := range nums {
		if nums[i] != 0 {
			continue
		}

		right := append([]int{}, nums...)
		right = simulateMovement(i, right, 1)
		if isAllZero(right) {
			count += 1
		}

		left := append([]int{}, nums...)
		left = simulateMovement(i, left, -1)
		if isAllZero(left) {
			count += 1
		}
	}
	return count
}

func simulateMovement(p int, array []int, sign int) []int {
	for p < len(array) && p >= 0 {
		if array[p] == 0 {
			p += sign
			continue
		} else {
			array[p] -= 1
		}

		sign *= -1
		p += sign
	}
	return array
}

func isAllZero(array []int) bool {
	for _, num := range array {
		if num != 0 {
			return false
		}
	}
	return true
}
