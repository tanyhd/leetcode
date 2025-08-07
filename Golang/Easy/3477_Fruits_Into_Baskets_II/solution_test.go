package solution

import "testing"

func TestNumOfUnplacedFruits(t *testing.T) {
	tests := []struct {
		name     string
		fruits   []int
		baskets  []int
		expected int
	}{
		{"Case 1", []int{4, 2, 5}, []int{3, 5, 4}, 1},
		{"Case 2", []int{3, 6, 1}, []int{6, 4, 7}, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := numOfUnplacedFruits(tt.fruits, tt.baskets)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
