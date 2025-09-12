package vowelsgameinastring

import (
	"testing"
)

func TestDoesAliceWin(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected bool
	}{
		{"Case 1", "leetcoder", true},
		{"Case 2", "bbcd", false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := doesAliceWin(tt.s)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
