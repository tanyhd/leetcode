package findtheminimumareatocoverallonesi

import (
	"testing"
)

func TestMinimumArea(t *testing.T) {
	tests := []struct {
		name     string
		grid     [][]int
		expected int
	}{
		{"Case 1", [][]int{{0, 1, 0}, {1, 0, 1}}, 6},
		{"Case 2", [][]int{{1, 0}, {0, 0}}, 1},
		{"Case 3", [][]int{{0}, {1}}, 1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minimumArea(tt.grid)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
