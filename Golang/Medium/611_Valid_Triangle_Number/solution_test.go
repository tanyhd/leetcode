package validtrianglenumber

import "testing"

func TestTriangleNumber(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{2, 2, 3, 4}, 3},
		{"Case 2", []int{4, 2, 3, 4}, 4},
		{"Case 3", []int{48, 66, 61, 46, 94, 75}, 19},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := triangleNumber(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
