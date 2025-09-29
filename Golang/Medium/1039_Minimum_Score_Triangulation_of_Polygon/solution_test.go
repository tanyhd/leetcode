package minimumscoretriangulationofpolygon

import (
	"testing"
)

func TestMinScoreTriangulation(t *testing.T) {
	tests := []struct {
		name     string
		values   []int
		expected int
	}{
		{"Case 1", []int{1, 2, 3}, 6},
		{"Case 2", []int{3, 7, 4, 5}, 144},
		{"Case 3", []int{1, 3, 1, 4, 1, 5}, 13},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minScoreTriangulation(tt.values)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
