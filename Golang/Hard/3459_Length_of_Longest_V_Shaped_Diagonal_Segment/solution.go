package lengthoflongestvshapeddiagonalsegment

type state struct {
	r                int
	c                int
	prev             int
	currentDirection string
	hasMadeTurn      bool
}

func lenOfVDiagonal(grid [][]int) int {
	directions := map[string][]int{
		"leftTop":  {-1, -1},
		"leftBot":  {1, -1},
		"rightTop": {-1, 1},
		"rightBot": {1, 1},
	}

	clockwise := map[string]string{
		"leftTop":  "rightTop",
		"rightTop": "rightBot",
		"rightBot": "leftBot",
		"leftBot":  "leftTop",
	}

	maxCount := 0
	memo := make(map[state]int)

	for r := range grid {
		for c := range grid[0] {
			if grid[r][c] == 1 {
				for d, _ := range directions {
					dr := directions[d][0]
					dc := directions[d][1]
					maxCount = max(maxCount, 1+explore(r+dr, c+dc, grid, 1, d, false, directions, clockwise, memo))
				}
			}
		}
	}
	return maxCount
}

func explore(r int, c int, grid [][]int, prev int, currentDirection string, hasMadeTurn bool, directions map[string][]int, clockwise map[string]string, memo map[state]int) int {
	if !inbound(r, c, grid) {
		return 0
	}

	key := state{r, c, prev, currentDirection, hasMadeTurn}
	if v, exist := memo[key]; exist {
		return v
	}

	if grid[r][c] == 1 {
		return 0
	}

	if prev == 1 && grid[r][c] != 2 {
		return 0
	}

	if prev == 2 && grid[r][c] != 0 {
		return 0
	}

	if prev == 0 && grid[r][c] != 2 {
		return 0
	}

	maxPath := 0
	dr := directions[currentDirection][0]
	dc := directions[currentDirection][1]

	maxPath = max(maxPath, explore(r+dr, c+dc, grid, grid[r][c], currentDirection, hasMadeTurn, directions, clockwise, memo))

	if !hasMadeTurn {
		newDirection := clockwise[currentDirection]
		dr := directions[newDirection][0]
		dc := directions[newDirection][1]
		maxPath = max(maxPath, explore(r+dr, c+dc, grid, grid[r][c], newDirection, true, directions, clockwise, memo))
	}

	memo[key] = maxPath + 1
	return memo[key]
}

func inbound(r int, c int, grid [][]int) bool {
	rInbound := r >= 0 && r < len(grid)
	cInbound := c >= 0 && c < len(grid[0])
	return rInbound && cInbound
}
