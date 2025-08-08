package twosum

import (
	"slices"
	"testing"
)

func TestTwoSum(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		target   int
		expected []int
	}{
		{"Case 1", []int{2, 7, 11, 15}, 9, []int{0, 1}},
		{"Case 2", []int{3, 2, 4}, 6, []int{1, 2}},
		{"Case 3", []int{3, 3}, 6, []int{0, 1}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := twoSum(tt.nums, tt.target)
			if !slices.Equal(tt.expected, result) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
