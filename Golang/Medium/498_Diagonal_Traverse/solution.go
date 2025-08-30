package diagonaltraverse

func findDiagonalOrder(mat [][]int) []int {
	output := []int{}
	side := 0

	for r := range len(mat) {
		for c := range len(mat[0]) {
			if r == 0 {
				ls := []int{}
				explore(r, c, mat, &ls)
				appendOutput(&output, side, ls)
				side += 1
			} else if c == len(mat[0])-1 {
				ls := []int{}
				explore(r, c, mat, &ls)
				appendOutput(&output, side, ls)
				side += 1
			}
		}
	}
	return output
}

func explore(r int, c int, mat [][]int, ls *[]int) {
	if !inbound(r, c, mat) {
		return
	}
	*ls = append(*ls, mat[r][c])
	explore(r+1, c-1, mat, ls)
}

func inbound(r int, c int, mat [][]int) bool {
	rInbound := r >= 0 && r < len(mat)
	cInbound := c >= 0 && c < len(mat[0])
	return rInbound && cInbound
}

func appendOutput(output *[]int, side int, ls []int) {
	if side%2 == 0 {
		for len(ls) != 0 {
			temp := ls[len(ls)-1]
			ls = ls[:len(ls)-1]
			*output = append(*output, temp)
		}
	} else {
		*output = append(*output, ls...)
	}
}
