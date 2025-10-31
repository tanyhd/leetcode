package thetwosneakynumbersofdigitville

func getSneakyNumbers(nums []int) []int {
	numMap := make(map[int]int)
	output := []int{}

	for _, num := range nums {
		if _, exist := numMap[num]; exist {
			output = append(output, num)
		} else {
			numMap[num] = 1
		}
	}
	return output
}
