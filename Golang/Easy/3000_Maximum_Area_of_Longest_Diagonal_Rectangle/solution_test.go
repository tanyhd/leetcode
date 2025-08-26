package maximumareaoflongestdiagonalrectangle

import "testing"

func TestAreaOfMaxDiagonal(t *testing.T) {
	tests := []struct {
		name       string
		dimensions [][]int
		expected   int
	}{
		{"Case 1", [][]int{{9, 3}, {8, 6}}, 48},
		{"Case 2", [][]int{{3, 4}, {4, 3}}, 12},
		{"Case 3", [][]int{{6, 5}, {8, 6}, {2, 10}, {8, 1}, {9, 2}, {3, 5}, {3, 5}}, 20},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := areaOfMaxDiagonal(tt.dimensions)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
