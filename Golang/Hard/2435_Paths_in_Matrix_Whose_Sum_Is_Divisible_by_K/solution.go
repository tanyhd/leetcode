package pathsinmatrixwhosesumisdivisiblebyk

type state struct {
	r   int
	c   int
	rem int
}

func numberOfPaths(grid [][]int, k int) int {
	return explore(0, 0, grid, 0, k, make(map[state]int))
}

func explore(r int, c int, grid [][]int, rem int, k int, memo map[state]int) int {
	if !inbound(r, c, grid) {
		return 0
	}

	const mod = 1_000_000_007
	rem = (rem + grid[r][c]) % k
	key := state{r, c, rem}
	if v, exist := memo[key]; exist {
		return v
	}

	if r == len(grid)-1 && c == len(grid[0])-1 {
		if rem == 0 {
			return 1
		}
		return 0
	}

	down := explore(r+1, c, grid, rem, k, memo)
	right := explore(r, c+1, grid, rem, k, memo)
	memo[key] = (down + right) % mod
	return memo[key]
}

func inbound(r int, c int, grid [][]int) bool {
	rInbound := r >= 0 && r < len(grid)
	cInbound := c >= 0 && c < len(grid[0])
	return rInbound && cInbound
}
