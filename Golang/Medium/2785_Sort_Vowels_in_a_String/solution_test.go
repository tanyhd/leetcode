package sortvowelsinastring

import (
	"testing"
)

func TestSortVowels(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected string
	}{
		{"Case 1", "lEetcOde", "lEOtcede"},
		{"Case 2", "lYmpH", "lYmpH"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := sortVowels(tt.s)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
