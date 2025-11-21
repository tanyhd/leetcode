package uniquelength3palindromicsubsequences

import (
	"testing"
)

func TestCountPalindromicSubsequence(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected int
	}{
		{"Case 1", "aabca", 3},
		{"Case 2", "adc", 0},
		{"Case 3", "bbcbaba", 4},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := countPalindromicSubsequence(tt.s)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
