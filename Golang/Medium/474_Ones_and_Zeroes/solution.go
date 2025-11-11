package onesandzeroes

type state struct {
	p int
	m int
	n int
}

func findMaxForm(strs []string, m int, n int) int {
	return helper(strs, 0, m, n, make(map[state]int))
}

func helper(s []string, p int, m int, n int, memo map[state]int) int {
	key := state{p, m, n}
	if v, exist := memo[key]; exist {
		return v
	}

	if p >= len(s) {
		return 0
	}

	currentS := s[p]
	mCount := 0
	nCount := 0
	for _, c := range currentS {
		if c == '1' {
			nCount += 1
		}
		if c == '0' {
			mCount += 1
		}
	}

	include := 0
	if mCount <= m && nCount <= n {
		include = helper(s, p+1, m-mCount, n-nCount, memo) + 1
	}

	exclude := helper(s, p+1, m, n, memo)
	memo[key] = max(include, exclude)
	return memo[key]
}
