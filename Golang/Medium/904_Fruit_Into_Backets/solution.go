package fruitintobackets

func totalFruit(fruits []int) int {
	p1 := 0
	p2 := p1 + 1
	fMap := make(map[int]int)
	fMap[fruits[p1]] = 1
	maxCount := 1

	for p2 < len(fruits) {
		f := fruits[p2]
		fMap[f] += 1

		if len(fMap) <= 2 {
			count := 0
			for key, _ := range fMap {
				count += fMap[key]
			}
			maxCount = max(maxCount, count)
			p2 += 1
		} else {
			f := fruits[p1]
			fMap[f] -= 1
			if fMap[f] == 0 {
				delete(fMap, f)
			}
			p1 += 1
			p2 += 1
		}
	}

	return maxCount
}
