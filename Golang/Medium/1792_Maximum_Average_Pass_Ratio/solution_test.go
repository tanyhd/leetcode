package maximumaveragepassratio

import (
	"testing"
)

func TestMaxAverageRatio(t *testing.T) {
	tests := []struct {
		name          string
		classes       [][]int
		extraStudents int
		expected      float64
	}{
		{"Case 1", [][]int{{1, 2}, {3, 5}, {2, 2}}, 2, 0.78333},
		{"Case 2", [][]int{{2, 4}, {3, 9}, {4, 5}, {2, 10}}, 4, 0.53485},
	}

	const epsilon = 1e-5

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxAverageRatio(tt.classes, tt.extraStudents)
			if diff := result - tt.expected; diff < -epsilon || diff > epsilon {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
