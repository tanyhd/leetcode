package replacenoncoprimenumbersinarray

import (
	"slices"
	"testing"
)

func TestReplaceNonCoprimes(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected []int
	}{
		{"Case 1", []int{6, 4, 3, 2, 7, 6, 2}, []int{12, 7, 6}},
		{"Case 2", []int{2, 2, 1, 1, 3, 3, 3}, []int{2, 1, 1, 3}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := replaceNonCoprimes(tt.nums)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
