package waterbottlesii

import (
	"testing"
)

func TestMaxBottlesDrunk(t *testing.T) {
	tests := []struct {
		name        string
		numBottles  int
		numExchange int
		expected    int
	}{
		{"Case 1", 13, 6, 15},
		{"Case 2", 10, 3, 13},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxBottlesDrunk(tt.numBottles, tt.numExchange)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
