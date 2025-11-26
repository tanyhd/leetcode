package pathsinmatrixwhosesumisdivisiblebyk

import "testing"

func TestNumberOfPaths(t *testing.T) {
	tests := []struct {
		name     string
		grid     [][]int
		k        int
		expected int
	}{
		{"Case 1", [][]int{{5, 2, 4}, {3, 0, 5}, {0, 7, 2}}, 3, 2},
		{"Case 2", [][]int{{0, 0}}, 5, 1},
		{"Case 3", [][]int{{7, 3, 4, 9}, {2, 3, 6, 2}, {2, 3, 7, 0}}, 1, 10},
		{"Case 4", [][]int{{1, 5, 3, 7, 3, 2, 3, 5}}, 29, 1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := numberOfPaths(tt.grid, tt.k)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
