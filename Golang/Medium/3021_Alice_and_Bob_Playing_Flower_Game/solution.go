package aliceandbobplayingflowergame

type state struct {
	n int
	m int
}

func flowerGame(n int, m int) int64 {
	return _flowerGame(n, m, make(map[state]int64))
}

func _flowerGame(n int, m int, memo map[state]int64) int64 {
	if n == 0 || m == 0 {
		return int64(0)
	}

	key := state{n, m}
	if v, exist := memo[key]; exist {
		return v
	}

	count := int64(0)
	if (n+m)%2 != 0 {
		count += 1
	}

	count += _flowerGame(n-1, m, memo)
	count += _flowerGame(n, m-1, memo)
	count -= _flowerGame(n-1, m-1, memo)
	memo[key] = count
	return count
}
