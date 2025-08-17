package new21game

func new21Game(n int, k int, maxPts int) float64 {
	return _new21Game(n, 0, k, maxPts, make(map[int]float64))
}

func _new21Game(n int, total int, k int, maxPts int, memo map[int]float64) float64 {
	if v, exist := memo[total]; exist {
		return v
	}
	if total >= k {
		if total <= n {
			return 1.0
		} else {
			return 0.0
		}
	}

	count := float64(0)
	for i := 1; i <= maxPts; i++ {
		count += _new21Game(n, total+i, k, maxPts, memo) / float64(maxPts)
	}
	memo[total] = count
	return count
}
