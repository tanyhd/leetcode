package largestperimetertriangle

import "testing"

func TestLargestPerimeter(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{2, 1, 2}, 5},
		{"Case 2", []int{1, 2, 1, 10}, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := largestPerimeter(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
