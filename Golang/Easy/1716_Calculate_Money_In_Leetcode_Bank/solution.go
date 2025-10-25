package calculatemoneyinleetcodebank

func totalMoney(n int) int {
	start := 1
	count := 0

	for i := 1; i <= n; i++ {
		count += start
		start += 1

		if i%7 == 0 {
			start = start - 7 + 1
		}
	}
	return count
}
