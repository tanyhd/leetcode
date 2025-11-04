package findxsumofallklongsubarraysi

import (
	"slices"
	"testing"
)

func TestFindXSum(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		k        int
		x        int
		expected []int
	}{
		{"Case 1", []int{1, 1, 2, 2, 3, 4, 2, 3}, 6, 2, []int{6, 10, 12}},
		{"Case 2", []int{3, 8, 7, 8, 7, 5}, 2, 2, []int{11, 15, 15, 15, 12}},
		{"Case 3", []int{9, 2, 2}, 3, 3, []int{13}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findXSum(tt.nums, tt.k, tt.x)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
