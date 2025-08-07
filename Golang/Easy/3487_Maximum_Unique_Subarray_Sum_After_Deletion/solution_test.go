package maximumuniquesubarraysumafterdeletion

import "testing"

func TestMaxSum(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{1, 2, 3, 4, 5}, 15},
		{"Case 2", []int{1, 1, 0, 1, 1}, 1},
		{"Case 3", []int{1, 2, -1, -2, 1, 0, -1}, 3},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxSum(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
