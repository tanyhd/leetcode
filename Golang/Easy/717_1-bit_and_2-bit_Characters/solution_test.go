package bitand2bitcharacters

import "testing"

func TestIsOneBitCharacter(t *testing.T) {
	tests := []struct {
		name     string
		bits     []int
		expected bool
	}{
		{"Case 1", []int{1, 0, 0}, true},
		{"Case 2", []int{1, 1, 1, 0}, false},
		{"Case 3", []int{0, 0}, true},
		{"Case 4", []int{1, 1, 0}, true},
		{"Case 5", []int{0, 1, 0}, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := isOneBitCharacter(tt.bits)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
