package greatestsumdivisiblebythree

import "testing"

func TestMaxSumDivThree(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{3, 6, 5, 1, 8}, 18},
		{"Case 2", []int{4}, 0},
		{"Case 3", []int{1, 2, 3, 4, 4}, 12},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxSumDivThree(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
