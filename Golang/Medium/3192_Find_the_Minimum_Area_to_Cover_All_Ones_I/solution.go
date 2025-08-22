package findtheminimumareatocoverallonesi

func minimumArea(grid [][]int) int {
	start := false
	pos := []int{}

	for r, _ := range grid {
		for c, _ := range grid[0] {
			if grid[r][c] == 1 {
				if !start {
					pos = append(pos, r)
					pos = append(pos, c)
					pos = append(pos, c)
					pos = append(pos, r)
					start = true
				} else {
					tr := pos[0]
					if r < tr {
						pos[0] = r
					}

					lc := pos[1]
					if c < lc {
						pos[1] = c
					}

					rc := pos[2]
					if c > rc {
						pos[2] = c
					}

					br := pos[3]
					if r > br {
						pos[3] = r
					}
				}
			}
		}
	}

	height := pos[3] - pos[0] + 1
	width := pos[2] - pos[1] + 1
	return height * width
}
