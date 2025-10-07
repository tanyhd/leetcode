package avoidfloodinthecity

import (
	"slices"
	"sort"
)

func avoidFlood(rains []int) []int {
	output := slices.Repeat([]int{1}, len(rains))
	lastWetDay := make(map[int]int)
	dryDays := []int{}

	for i, lake := range rains {
		if lake == 0 {
			dryDays = append(dryDays, i)
		} else {
			output[i] = -1

			if _, exist := lastWetDay[lake]; exist {
				dryDayIndex := sort.Search(len(dryDays), func(i int) bool { return dryDays[i] > lastWetDay[lake] })
				if dryDayIndex == len(dryDays) {
					return []int{}
				}
				d := dryDays[dryDayIndex]
				dryDays = slices.Delete(dryDays, dryDayIndex, dryDayIndex+1)
				output[d] = lake
			}
			lastWetDay[lake] = i
		}
	}
	return output
}
