package waystoexpressanintegerassumofpowers

import "math"

type state struct {
	n   int
	pos int
}

func numberOfWays(n int, x int) int {
	powers := []int{}
	for i := 1; i <= n; i++ {
		numPow := int(math.Pow(float64(i), float64(x)))
		if numPow <= n {
			powers = append(powers, numPow)
		}
	}
	return _numberOfWays(n, x, powers, 0, make(map[state]int))
}

func _numberOfWays(n int, x int, powers []int, pos int, memo map[state]int) int {
	const mod = 1_000_000_007
	key := state{n, pos}
	if v, exist := memo[key]; exist {
		return v
	}
	if n == 0 {
		return 1
	}
	if n < 0 {
		return 0
	}
	if pos >= len(powers) {
		return 0
	}

	num := powers[pos]
	count := 0
	count += _numberOfWays(n, x, powers, pos+1, memo)
	count += _numberOfWays(n-num, x, powers, pos+1, memo)
	memo[key] = count % mod
	return memo[key]
}
