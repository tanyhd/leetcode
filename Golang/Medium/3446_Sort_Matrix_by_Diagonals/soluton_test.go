package sortmatrixbydiagonals

import (
	"reflect"
	"testing"
)

func TestSortMatrix(t *testing.T) {
	tests := []struct {
		name     string
		grid     [][]int
		expected [][]int
	}{
		{"Case 1", [][]int{{1, 7, 3}, {9, 8, 2}, {4, 5, 6}}, [][]int{{8, 2, 3}, {9, 6, 7}, {4, 5, 1}}},
		{"Case 2", [][]int{{0, 1}, {1, 2}}, [][]int{{2, 1}, {1, 0}}},
		{"Case 3", [][]int{{1}}, [][]int{{1}}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := sortMatrix(tt.grid)
			if !reflect.DeepEqual(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
