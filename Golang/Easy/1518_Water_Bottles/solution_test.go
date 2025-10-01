package waterbottles

import "testing"

func TestNumWaterBottles(t *testing.T) {
	tests := []struct {
		name        string
		numBottles  int
		numExchange int
		expected    int
	}{
		{"Case 1", 9, 3, 13},
		{"Case 2", 15, 4, 19},
		{"Case 3", 5, 5, 6},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := numWaterBottles(tt.numBottles, tt.numExchange)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
