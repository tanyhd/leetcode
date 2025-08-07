package maximumscorefromremovingsubstrings

func maximumGain(s string, x int, y int) int {
	main := ""
	sub := ""
	mainPoint := 0
	subPoint := 0

	if x > y {
		main = "ab"
		mainPoint = x
		sub = "ba"
		subPoint = y
	} else {
		main = "ba"
		mainPoint = y
		sub = "ab"
		subPoint = x
	}

	stack := []string{}

	//first pass
	for _, c := range s {
		c := string(c)
		if len(stack) != 0 && stack[len(stack)-1]+c == main {
			stack = stack[:len(stack)-1]
			continue
		} else {
			stack = append(stack, c)
		}
	}

	points := ((len(s) - len(stack)) / 2) * mainPoint

	stack2 := []string{}
	//second pass
	for _, c := range stack {
		if len(stack2) != 0 && stack2[len(stack2)-1]+c == sub {
			stack2 = stack2[:len(stack2)-1]
			continue
		} else {
			stack2 = append(stack2, c)
		}
	}

	points += ((len(stack) - len(stack2)) / 2) * subPoint

	return points
}
