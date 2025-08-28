package sortmatrixbydiagonals

import "sort"

func sortMatrix(grid [][]int) [][]int {

	for r := range grid {
		for c := range grid[0] {
			if r == 0 || c == 0 {
				ls := []int{}
				explore(r, c, grid, &ls)

				if r == 0 && c == 0 {
					sort.Slice(ls, func(i int, j int) bool {
						return ls[i] > ls[j]
					})
				} else if r == 0 {
					sort.Slice(ls, func(i int, j int) bool {
						return ls[i] < ls[j]
					})
				} else {
					sort.Slice(ls, func(i int, j int) bool {
						return ls[i] > ls[j]
					})
				}
				exploreUpdate(r, c, grid, &ls, 0)
			}
		}
	}
	return grid
}

func explore(r int, c int, grid [][]int, ls *[]int) {
	if !inbound(r, c, grid) {
		return
	}
	*ls = append(*ls, grid[r][c])
	explore(r+1, c+1, grid, ls)
}

func exploreUpdate(r int, c int, grid [][]int, updateList *[]int, pos int) {
	if !inbound(r, c, grid) {
		return
	}
	grid[r][c] = (*updateList)[pos]
	exploreUpdate(r+1, c+1, grid, updateList, pos+1)
}

func inbound(r int, c int, grid [][]int) bool {
	rInbound := r >= 0 && r < len(grid)
	cInbound := c >= 0 && c < len(grid[0])
	return rInbound && cInbound
}
