package smallestmissingnonnegativeintegerafteroperations

import (
	"testing"
)

func TestFindSmallestInteger(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		value    int
		expected int
	}{
		{"Case 1", []int{1, -10, 7, 13, 6, 8}, 5, 4},
		{"Case 2", []int{1, -10, 7, 13, 6, 8}, 7, 2},
		{"Case 3", []int{3, 0, 3, 2, 4, 2, 1, 1, 0, 4}, 5, 10},
		{"Case 4", []int{0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1}, 2, 15},
		{"Case 5", []int{0, -3}, 4, 2},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findSmallestInteger(tt.nums, tt.value)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
