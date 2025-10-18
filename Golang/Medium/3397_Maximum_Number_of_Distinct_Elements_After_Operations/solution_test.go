package maximumnumberofdistinctelementsafteroperations

import (
	"testing"
)

func TestMaxDistinctElements(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		k        int
		expected int
	}{
		{"Case 1", []int{1, 2, 2, 3, 3, 4}, 2, 6},
		{"Case 2", []int{4, 4, 4, 4}, 1, 3},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maxDistinctElements(tt.nums, tt.k)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
