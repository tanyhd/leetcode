package takingmaximumenergyfromthemysticdungeon

import "math"

func maximumEnergy(energy []int, k int) int {
	maxEnergy := math.MinInt
	memo := make(map[int]int)
	for i, _ := range energy {
		maxEnergy = max(maxEnergy, explore(i, k, energy, memo))
	}
	return maxEnergy
}

func explore(p int, k int, energy []int, memo map[int]int) int {
	if p >= len(energy) {
		return 0
	}

	if v, exist := memo[p]; exist {
		return v
	}

	memo[p] = energy[p] + explore(p+k, k, energy, memo)
	return memo[p]
}
