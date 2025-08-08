package validparentheses

import "testing"

func TestIsValid(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected bool
	}{
		{"Case 1", "()", true},
		{"Case 2", "()[]{}", true},
		{"Case 3", "(]", false},
		{"Case 4", "([])", true},
		{"Case 5", "([)]", false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isValid(tt.s)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
