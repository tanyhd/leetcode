package rangeproductqueriesofpowers

import (
	"slices"
	"testing"
)

func TestProductQueries(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		queries  [][]int
		expected []int
	}{
		{"Case 1", 15, [][]int{{0, 1}, {2, 2}, {0, 3}}, []int{2, 4, 64}},
		{"Case 2", 2, [][]int{{0, 0}}, []int{2}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := productQueries(tt.n, tt.queries)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
