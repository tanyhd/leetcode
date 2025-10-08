package successfulpairsofspellsandpotions

import (
	"slices"
	"testing"
)

func TestSuccessfulPairs(t *testing.T) {
	tests := []struct {
		name     string
		spells   []int
		potions  []int
		success  int64
		expected []int
	}{
		{"Case 1", []int{5, 1, 3}, []int{1, 2, 3, 4, 5}, 7, []int{4, 0, 3}},
		{"Case 2", []int{3, 1, 2}, []int{8, 5, 8}, 16, []int{2, 0, 2}},
		{"Case 3", []int{15, 8, 19}, []int{38, 36, 23}, 328, []int{3, 0, 3}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := successfulPairs(tt.spells, tt.potions, tt.success)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
