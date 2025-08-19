package numberofzerofilledsubarrays

import (
	"testing"
)

func TestNumberOfWays(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int64
	}{
		{"Case 1", []int{1, 3, 0, 0, 2, 0, 0, 4}, 6},
		{"Case 2", []int{0, 0, 0, 2, 0, 0}, 9},
		{"Case 3", []int{2, 10, 2019}, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := zeroFilledSubarray(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
