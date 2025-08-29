package aliceandbobplayingflowergame

import (
	"testing"
)

func TestFlowerGame(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		m        int
		expected int64
	}{
		{"Case 1", 3, 2, 3},
		{"Case 2", 1, 1, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := flowerGame(tt.n, tt.m)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
