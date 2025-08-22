package maximumscorefromremovingsubstrings

import "testing"

func TestMaximumGain(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		x        int
		y        int
		expected int
	}{
		{"Case 1", "cdbcbbaaabab", 4, 5, 19},
		{"Case 2", "aabbaaxybbaabb", 5, 4, 20},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maximumGain(tt.s, tt.x, tt.y)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
