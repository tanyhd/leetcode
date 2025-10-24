package nextgreaternumericallybalancednumber

func nextBeautifulNumber(n int) int {
	n += 1
	for !isNumBalance(n) {
		n += 1
	}
	return n
}

func isNumBalance(n int) bool {
	numMap := make(map[int]int)

	for n > 0 {
		r := n % 10
		numMap[r] += 1
		n = n / 10
	}

	for num, value := range numMap {
		if num != value {
			return false
		}
	}
	return true
}
