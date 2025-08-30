package validsudoku

func isValidSudoku(board [][]byte) bool {
	for r := range board {
		for c := range board[0] {
			if r == 0 {
				if !checkCol(r, c, board, make(map[byte]struct{})) {
					return false
				}
			}
			if c == 0 {
				if !checkRow(r, c, board, make(map[byte]struct{})) {
					return false
				}
			}
			if r%3 == 0 && c%3 == 0 {
				if !checkBox(r, c, board) {
					return false
				}
			}
		}
	}
	return true
}

func checkRow(r int, c int, board [][]byte, numMap map[byte]struct{}) bool {
	if !inbound(r, c, board) {
		return true
	}
	cNum := board[r][c]
	if _, exist := numMap[cNum]; exist {
		return false
	}
	if cNum != '.' {
		numMap[cNum] = struct{}{}
	}
	return checkRow(r, c+1, board, numMap)
}

func checkCol(r int, c int, board [][]byte, numMap map[byte]struct{}) bool {
	if !inbound(r, c, board) {
		return true
	}
	cNum := board[r][c]
	if _, exist := numMap[cNum]; exist {
		return false
	}
	if cNum != '.' {
		numMap[cNum] = struct{}{}
	}
	return checkCol(r+1, c, board, numMap)
}

func checkBox(r int, c int, board [][]byte) bool {
	numMap := make(map[byte]struct{})
	for i := range 3 {
		for j := range 3 {
			cR := r + i
			cC := c + j

			cNum := board[cR][cC]
			if _, exist := numMap[cNum]; exist {
				return false
			}
			if cNum != '.' {
				numMap[cNum] = struct{}{}
			}
		}
	}
	return true
}

func inbound(r int, c int, board [][]byte) bool {
	rInbound := r >= 0 && r < len(board)
	cInbound := c >= 0 && c < len(board[0])
	return rInbound && cInbound
}
