package makearrayelementsequaltozero

import "testing"

func TestCountValidSelections(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{1, 0, 2, 0, 3}, 2},
		{"Case 2", []int{2, 3, 4, 0, 4, 1, 0}, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := countValidSelections(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
