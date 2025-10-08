package successfulpairsofspellsandpotions

import "sort"

func successfulPairs(spells []int, potions []int, success int64) []int {
	output := []int{}
	sort.Ints(potions)

	for i, _ := range spells {
		count := 0

		p1 := 0
		p2 := len(potions) - 1

		for p1 <= p2 {
			mid := (p1 + p2) / 2
			power := int64(spells[i] * potions[mid])
			if power < success {
				p1 = mid + 1
			} else {
				p2 = mid - 1
			}
		}
		count += len(potions) - p1
		output = append(output, count)
	}
	return output
}
