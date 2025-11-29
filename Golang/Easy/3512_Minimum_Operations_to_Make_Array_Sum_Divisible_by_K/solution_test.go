package minimumoperationstomakearraysumdivisiblebyk

import "testing"

func TestMinOperations(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		k        int
		expected int
	}{
		{"Case 1", []int{3, 9, 7}, 5, 4},
		{"Case 2", []int{4, 1, 3}, 4, 0},
		{"Case 3", []int{3, 2}, 6, 5},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minOperations(tt.nums, tt.k)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
