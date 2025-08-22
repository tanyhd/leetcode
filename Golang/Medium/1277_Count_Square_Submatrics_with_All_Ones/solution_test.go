package countsquaresubmatricswithallones

import (
	"testing"
)

func TestCountSquares(t *testing.T) {
	tests := []struct {
		name     string
		matrix   [][]int
		expected int
	}{
		{"Case 1", [][]int{{0, 1, 1, 1}, {1, 1, 1, 1}, {0, 1, 1, 1}}, 15},
		{"Case 2", [][]int{{1, 0, 1}, {1, 1, 0}, {1, 1, 0}}, 7},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := countSquares(tt.matrix)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
