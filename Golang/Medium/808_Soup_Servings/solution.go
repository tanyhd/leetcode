package soupservings

import "strconv"

func soupServings(n int) float64 {
	if n > 4800 {
		return 1.0
	}
	return _soupServings(n, n, make(map[string]float64))
}

func _soupServings(a int, b int, memo map[string]float64) float64 {
	key := strconv.Itoa(a) + "," + strconv.Itoa(b)
	if v, exist := memo[key]; exist {
		return v
	}
	if a <= 0 && b > 0 {
		return 1.0
	}
	if a <= 0 && b <= 0 {
		return 0.5
	}
	if a > 0 && b <= 0 {
		return 0.0
	}

	count := 0.0
	count += _soupServings(a-100, b, memo)
	count += _soupServings(a-75, b-25, memo)
	count += _soupServings(a-50, b-50, memo)
	count += _soupServings(a-25, b-75, memo)
	memo[key] = 0.25 * count
	return memo[key]
}
