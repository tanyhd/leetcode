package poweroffour

import "testing"

func TestIsPowerOfFour(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected bool
	}{
		{"Case 1", 16, true},
		{"Case 2", 5, false},
		{"Case 3", 1, true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isPowerOfFour(tt.n)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
