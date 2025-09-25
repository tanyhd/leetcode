package triangle

type state struct {
	r int
	c int
}

func minimumTotal(triangle [][]int) int {
	return explore(0, 0, triangle, make(map[state]int))
}

func explore(r int, c int, grid [][]int, memo map[state]int) int {
	if !inbound(r, c, grid) {
		return 0
	}

	key := state{r, c}
	if v, exist := memo[key]; exist {
		return v
	}

	left := explore(r+1, c, grid, memo)
	right := explore(r+1, c+1, grid, memo)
	memo[key] = grid[r][c] + min(left, right)
	return memo[key]
}

func inbound(r int, c int, grid [][]int) bool {
	rInbound := r >= 0 && r < len(grid)
	if !rInbound {
		return false
	}
	cInbound := c >= 0 && c < len(grid[r])
	return cInbound
}
