package finalvalueofvariableafterperformingoperations

func finalValueAfterOperations(operations []string) int {
	opValue := map[string]int{
		"--X": -1,
		"X--": -1,
		"++X": 1,
		"X++": 1,
	}
	x := 0

	for _, op := range operations {
		x += opValue[op]
	}

	return x
}
