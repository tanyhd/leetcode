package triangle

import "testing"

func TestMinimumTotal(t *testing.T) {
	tests := []struct {
		name     string
		triangle [][]int
		expected int
	}{
		{"Case 1", [][]int{{2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3}}, 11},
		{"Case 2", [][]int{{-10}}, -10},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minimumTotal(tt.triangle)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
