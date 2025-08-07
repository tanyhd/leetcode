package pascaltriangle

func generate(numRows int) [][]int {
	if numRows == 1 {
		return [][]int{{1}}
	}
	if numRows == 2 {
		return [][]int{{1}, {1, 1}}
	}

	rows := generate(numRows - 1)
	lastRow := rows[len(rows)-1]

	newRow := []int{1}
	for i := 0; i < len(lastRow)-1; i++ {
		newRow = append(newRow, lastRow[i]+lastRow[i+1])
	}
	newRow = append(newRow, 1)
	rows = append(rows, newRow)
	return rows
}
