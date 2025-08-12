package waystoexpressanintegerassumofpowers

import (
	"testing"
)

func TestNumberOfWays(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		x        int
		expected int
	}{
		{"Case 1", 10, 2, 1},
		{"Case 2", 4, 1, 2},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := numberOfWays(tt.n, tt.x)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
