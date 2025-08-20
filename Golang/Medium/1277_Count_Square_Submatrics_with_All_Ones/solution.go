package countsquaresubmatricswithallones

type state struct {
	row int
	col int
}

func countSquares(matrix [][]int) int {
	totalCount := 0
	for r, _ := range matrix {
		for c, _ := range matrix[0] {
			totalCount += explore(r, c, matrix, make(map[state]int))
		}
	}
	return totalCount
}

func explore(r int, c int, matrix [][]int, memo map[state]int) int {
	if !inbound(r, c, matrix) {
		return 0
	}

	key := state{r, c}
	if v, exist := memo[key]; exist {
		return v
	}

	if matrix[r][c] == 0 {
		return 0
	}

	up := explore(r-1, c, matrix, memo)
	left := explore(r, c-1, matrix, memo)
	diagonal := explore(r-1, c-1, matrix, memo)
	size := 1 + min(up, left, diagonal)

	memo[key] = size
	return size

}

func inbound(r int, c int, matrix [][]int) bool {
	rInbound := r >= 0 && r < len(matrix)
	cInbound := c >= 0 && c < len(matrix[0])
	return rInbound && cInbound
}
