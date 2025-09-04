package findclosestperson

import "testing"

func TestFindClosest(t *testing.T) {
	tests := []struct {
		name     string
		x        int
		y        int
		z        int
		expected int
	}{
		{"Case 1", 2, 7, 4, 1},
		{"Case 2", 2, 5, 6, 2},
		{"Case 3", 1, 5, 3, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findClosest(tt.x, tt.y, tt.z)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
