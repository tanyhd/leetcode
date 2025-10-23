package checkifdigitsareequalinstringafteroperationsi

import "testing"

func TestHasSameDigits(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected bool
	}{
		{"Case 1", "3902", true},
		{"Case 2", "34789", false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := hasSameDigits(tt.s)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
