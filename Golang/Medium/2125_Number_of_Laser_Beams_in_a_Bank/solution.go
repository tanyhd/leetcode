package numberoflaserbeamsinabank

func numberOfBeams(bank []string) int {
	bankArray := []int{}

	for r, _ := range bank {
		count := 0
		for c, _ := range bank[0] {
			if bank[r][c] == '1' {
				count += 1
			}
		}
		if count != 0 {
			bankArray = append(bankArray, count)
		}
	}

	total := 0
	for i := 0; i < len(bankArray)-1; i++ {
		total += bankArray[i] * bankArray[i+1]
	}
	return total
}
