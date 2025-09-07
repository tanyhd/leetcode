package findnuniqueintegerssumuptozero

func sumZero(n int) []int {
	output := []int{}
	count := 0
	for i := 1; i <= n; i++ {
		if i == n {
			output = append(output, count*-1)
		} else {
			count += i
			output = append(output, i)
		}
	}
	return output
}
