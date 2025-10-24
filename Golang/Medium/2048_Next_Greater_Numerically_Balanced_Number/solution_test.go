package nextgreaternumericallybalancednumber

import (
	"testing"
)

func TestNextBeautifulNumber(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected int
	}{
		{"Case 1", 1, 22},
		{"Case 2", 1000, 1333},
		{"Case 3", 3000, 3133},
		{"Case 4", 212, 221},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := nextBeautifulNumber(tt.n)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
