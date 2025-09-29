package minimumscoretriangulationofpolygon

import "math"

type state struct {
	i int
	j int
}

func minScoreTriangulation(values []int) int {
	return helper(values, 0, len(values)-1, make(map[state]int))
}

func helper(v []int, i int, j int, memo map[state]int) int {
	if j-i < 2 {
		return 0
	}

	key := state{i, j}
	if v, exist := memo[key]; exist {
		return v
	}

	minScore := math.MaxInt64
	for k := i + 1; k < j; k++ {
		score := v[i]*v[j]*v[k] + helper(v, i, k, memo) + helper(v, k, j, memo)
		minScore = min(minScore, score)
	}

	memo[key] = minScore
	return minScore
}
