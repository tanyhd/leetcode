package minimumoperationstomaketheintegerzero

import (
	"math"
	"math/bits"
)

const INF = int(1e18)

type state struct {
	num1 int
	k    int
}

// TLE brute force
func makeTheIntegerZeroV1(num1 int, num2 int) int {
	ops := _makeTheIntegerZeroV1(num1, num2, 0, make(map[state]int))
	if ops == INF {
		return -1
	}
	return ops
}

func _makeTheIntegerZeroV1(num1 int, num2 int, k int, memo map[state]int) int {

	if num1 < 0 {
		return INF
	}

	if num1 == 0 {
		return k
	}

	if k > 60 {
		return INF
	}

	key := state{num1, k}
	if v, exist := memo[key]; exist {
		return v
	}

	count := INF
	for i := range 61 {
		newNum := num1 - (int(math.Pow(2, float64(i))) + num2)
		count = min(count, _makeTheIntegerZeroV1(newNum, num2, k+1, memo))
	}

	memo[key] = count
	return count
}

func makeTheIntegerZeroV2(num1 int, num2 int) int {
	for k := range 61 {
		target := num1 - (k * num2)
		if target < 0 {
			continue
		}

		if bits.OnesCount(uint(target)) <= k && k <= target {
			return k
		}
	}
	return -1
}
