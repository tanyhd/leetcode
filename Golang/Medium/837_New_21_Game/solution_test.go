package new21game

import (
	"math"
	"testing"
)

func TestNew21Game(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		k        int
		maxPts   int
		expected float64
	}{
		{"Case 1", 10, 1, 10, 1.0},
		{"Case 2", 6, 1, 10, 0.6},
		{"Case 3", 21, 17, 10, 0.73278},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := new21Game(tt.n, tt.k, tt.maxPts)
			if math.Abs(result-tt.expected) > 1e-5 {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
