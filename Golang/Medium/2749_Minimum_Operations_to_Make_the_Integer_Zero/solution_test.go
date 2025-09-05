package minimumoperationstomaketheintegerzero

import (
	"testing"
)

func TestMakeTheIntegerZero(t *testing.T) {
	tests := []struct {
		name     string
		num1     int
		num2     int
		expected int
	}{
		{"Case 1", 3, -2, 3},
		{"Case 2", 5, 7, -1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := makeTheIntegerZeroV1(tt.num1, tt.num2)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
