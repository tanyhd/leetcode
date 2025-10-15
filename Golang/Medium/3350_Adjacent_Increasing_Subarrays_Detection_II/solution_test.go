package adjacentincreasingsubarraysdetectionii

import (
	"testing"
)

func TestMaxIncreasingSubarrays(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{2, 5, 7, 8, 9, 2, 3, 4, 3, 1}, 3},
		{"Case 2", []int{1, 2, 3, 4, 4, 4, 4, 5, 6, 7}, 2},
		{"Case 3", []int{-15, 19}, 1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxIncreasingSubarrays(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
