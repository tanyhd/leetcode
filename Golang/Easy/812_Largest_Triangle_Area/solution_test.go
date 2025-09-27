package largesttrianglearea

import "testing"

func TestLargestTriangleArea(t *testing.T) {
	tests := []struct {
		name     string
		points   [][]int
		expected float64
	}{
		{"Case 1", [][]int{{0, 0}, {0, 1}, {1, 0}, {0, 2}, {2, 0}}, 2},
		{"Case 2", [][]int{{1, 0}, {0, 0}, {0, 1}}, 0.5},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := largestTriangleArea(tt.points)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
