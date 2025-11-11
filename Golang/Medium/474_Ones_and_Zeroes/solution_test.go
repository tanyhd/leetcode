package onesandzeroes

import "testing"

func TestFindMaxForm(t *testing.T) {
	tests := []struct {
		name     string
		strs     []string
		m        int
		n        int
		expected int
	}{
		{"Case 1", []string{"10", "0001", "111001", "1", "0"}, 5, 3, 4},
		{"Case 2", []string{"10", "0", "1"}, 1, 1, 2},
		{"Case 3", []string{"10", "0001", "111001", "1", "0"}, 4, 3, 3},
		{"Case 4", []string{"00", "000"}, 1, 10, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findMaxForm(tt.strs, tt.m, tt.n)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
