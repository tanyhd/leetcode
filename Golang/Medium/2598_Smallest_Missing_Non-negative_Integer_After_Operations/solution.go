package smallestmissingnonnegativeintegerafteroperations

func findSmallestInteger(nums []int, value int) int {
	freq := make(map[int]int)

	for _, num := range nums {
		num = num % value
		if num < 0 {
			num += value
		}
		freq[num] += 1
	}

	p := 0
	for true {
		num := p % value
		if _, exist := freq[num]; !exist {
			return p
		}
		if freq[num] == 0 {
			return p
		}
		freq[num] -= 1
		p += 1
	}
	return 0
}
