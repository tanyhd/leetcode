package minimumtimetomakeropecolorful

import "testing"

func TestMinCost(t *testing.T) {
	tests := []struct {
		name       string
		colors     string
		neededTime []int
		expected   int
	}{
		{"Case 1", "abaac", []int{1, 2, 3, 4, 5}, 3},
		{"Case 2", "abc", []int{1, 2, 3}, 0},
		{"Case 3", "aabaa", []int{1, 2, 3, 4, 1}, 2},
		{"Case 4", "aaabbbabbbb", []int{3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1}, 26},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minCost(tt.colors, tt.neededTime)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
