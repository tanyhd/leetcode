package numberoflaserbeamsinabank

import (
	"testing"
)

func TestNumberOfBeams(t *testing.T) {
	tests := []struct {
		name     string
		bank     []string
		expected int
	}{
		{"Case 1", []string{"011001", "000000", "010100", "001000"}, 8},
		{"Case 2", []string{"000", "111", "000"}, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := numberOfBeams(tt.bank)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
