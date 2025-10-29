package smallestnumberwithallsetbits

import "testing"

func TestSmallestNumber(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected int
	}{
		{"Case 1", 5, 7},
		{"Case 2", 10, 15},
		{"Case 3", 3, 3},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := smallestNumber(tt.n)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
