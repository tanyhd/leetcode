package keepmultiplyingfoundvaluesbytwo

func findFinalValue(nums []int, original int) int {
	numMap := make(map[int]int)

	for _, num := range nums {
		numMap[num] += 1
	}

	for true {
		if _, exist := numMap[original]; exist {
			original = original * 2
		} else {
			break
		}
	}

	return original
}
