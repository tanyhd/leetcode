package maximum69number

func maximum69Number(num int) int {
	numArray := []int{}

	for num%10 != 0 {
		numArray = append(numArray, num%10)
		num = num / 10
	}

	output := 0
	haveChange := false
	for i := len(numArray) - 1; i >= 0; i-- {
		if !haveChange && numArray[i] == 6 {
			output = output*10 + 9
			haveChange = true
		} else {
			output = output*10 + numArray[i]
		}
	}

	return output
}
