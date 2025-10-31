package thetwosneakynumbersofdigitville

import (
	"slices"
	"testing"
)

func TestGetSneakyNumbers(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected []int
	}{
		{"Case 1", []int{0, 1, 1, 0}, []int{1, 0}},
		{"Case 2", []int{0, 3, 2, 1, 3, 2}, []int{3, 2}},
		{"Case 3", []int{7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2}, []int{4, 5}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := getSneakyNumbers(tt.nums)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
