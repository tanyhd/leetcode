package findminimumoperationstomakeallelementsdivisiblebythree

import "testing"

func TestMinimumOperations(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{1, 2, 3, 4}, 3},
		{"Case 2", []int{3, 6, 9}, 0},
		{"Case 3", []int{8}, 1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minimumOperations(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
