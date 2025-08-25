package diagonaltraverse

import (
	"slices"
	"testing"
)

func TestFindDiagonalOrder(t *testing.T) {
	tests := []struct {
		name     string
		mat      [][]int
		expected []int
	}{
		{"Case 1", [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, []int{1, 2, 4, 7, 5, 3, 6, 8, 9}},
		{"Case 2", [][]int{{1, 2}, {3, 4}}, []int{1, 2, 3, 4}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findDiagonalOrder(tt.mat)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
