package powerofthree

import "testing"

func TestIsPowerOfThree(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected bool
	}{
		{"Case 1", 27, true},
		{"Case 2", 0, false},
		{"Case 3", -1, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isPowerOfThree(tt.n)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
