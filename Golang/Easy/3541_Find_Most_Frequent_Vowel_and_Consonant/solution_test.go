package findmostfrequentvowelandconsonant

import "testing"

func TestMaxFreqSum(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected int
	}{
		{"Case 1", "successes", 6},
		{"Case 2", "aeiaeia", 3},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxFreqSum(tt.s)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
