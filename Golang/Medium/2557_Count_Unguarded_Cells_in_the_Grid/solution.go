package countunguardedcellsinthegrid

type state struct {
	r int
	c int
}

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	wallMap := make(map[state]bool)
	for _, wall := range walls {
		wState := state{wall[0], wall[1]}
		wallMap[wState] = true
	}

	guardMap := make(map[state]bool)
	for _, guard := range guards {
		gState := state{guard[0], guard[1]}
		guardMap[gState] = true
	}

	seen := make(map[state]bool)

	direction := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	for _, guard := range guards {
		for _, dir := range direction {
			dr := dir[0]
			dc := dir[1]

			guardExplore(guard[0], guard[1], dr, dc, m, n, wallMap, guardMap, seen)
		}
	}
	return m*n - len(seen) - len(wallMap) - len(guardMap)
}

func guardExplore(r int, c int, dr int, dc int, m int, n int, wallMap map[state]bool, guardMap map[state]bool, seen map[state]bool) {
	r += dr
	c += dc

	if !inbound(r, c, m, n) {
		return
	}

	cState := state{r, c}

	if _, exist := wallMap[cState]; exist {
		return
	}

	if _, exist := guardMap[cState]; exist {
		return
	}

	seen[cState] = true
	guardExplore(r, c, dr, dc, m, n, wallMap, guardMap, seen)

}

func inbound(r int, c int, m int, n int) bool {
	rInbound := r >= 0 && r < m
	cInbound := c >= 0 && c < n
	return rInbound && cInbound
}
