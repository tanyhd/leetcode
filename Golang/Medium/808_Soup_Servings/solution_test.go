package soupservings

import "testing"

func TestSoupServings(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected float64
	}{
		{"Case 1", 50, 0.62500},
		{"Case 2", 100, 0.71875},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := soupServings(tt.n)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
