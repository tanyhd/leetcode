package findtriangularsumofanarray

import (
	"testing"
)

func TestTriangularSum(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{1, 2, 3, 4, 5}, 8},
		{"Case 2", []int{5}, 5},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := triangularSum(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
