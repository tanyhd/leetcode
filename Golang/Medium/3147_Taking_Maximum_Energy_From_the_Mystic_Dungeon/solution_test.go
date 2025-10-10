package takingmaximumenergyfromthemysticdungeon

import (
	"testing"
)

func TestMaximumEnergy(t *testing.T) {
	tests := []struct {
		name     string
		energy   []int
		k        int
		expected int
	}{
		{"Case 1", []int{5, 2, -10, -5, 1}, 3, 3},
		{"Case 2", []int{-2, -3, -1}, 2, -1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maximumEnergy(tt.energy, tt.k)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
