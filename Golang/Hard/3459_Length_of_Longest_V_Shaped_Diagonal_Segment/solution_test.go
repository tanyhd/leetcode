package lengthoflongestvshapeddiagonalsegment

import "testing"

func TestLenOfVDiagonal(t *testing.T) {
	tests := []struct {
		name     string
		grid     [][]int
		expected int
	}{
		{"Case 1", [][]int{{2, 2, 1, 2, 2}, {2, 0, 2, 2, 0}, {2, 0, 1, 1, 0}, {1, 0, 2, 2, 2}, {2, 0, 0, 2, 2}}, 5},
		{"Case 2", [][]int{{2, 2, 2, 2, 2}, {2, 0, 2, 2, 0}, {2, 0, 1, 1, 0}, {1, 0, 2, 2, 2}, {2, 0, 0, 2, 2}}, 4},
		{"Case 3", [][]int{{1, 2, 2, 2, 2}, {2, 2, 2, 2, 0}, {2, 0, 0, 0, 0}, {0, 0, 2, 2, 2}, {2, 0, 0, 2, 0}}, 5},
		{"Case 4", [][]int{{1}}, 1},
		{"Case 5", [][]int{{0, 0, 1, 0}, {0, 2, 2, 0}}, 3},
		{"Case 6", [][]int{{1, 1, 1, 2, 0, 0}, {0, 0, 0, 0, 1, 2}}, 2},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := lenOfVDiagonal(tt.grid)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
