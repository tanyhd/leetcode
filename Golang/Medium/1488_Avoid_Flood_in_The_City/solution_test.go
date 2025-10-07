package avoidfloodinthecity

import (
	"slices"
	"testing"
)

func TestAvoidFlood(t *testing.T) {
	tests := []struct {
		name     string
		rains    []int
		expected []int
	}{
		{"Case 1", []int{1, 2, 3, 4}, []int{-1, -1, -1, -1}},
		{"Case 2", []int{1, 2, 0, 0, 2, 1}, []int{-1, -1, 2, 1, -1, -1}},
		{"Case 3", []int{1, 2, 0, 1, 2}, []int{}},
		{"Case 4", []int{69, 0, 0, 0, 69}, []int{-1, 69, 1, 1, -1}},
		{"Case 5", []int{0, 1, 1}, []int{}},
		{"Case 6", []int{1, 0, 2, 0, 2, 1}, []int{-1, 1, -1, 2, -1, -1}},
		{"Case 7", []int{1, 0, 2, 0, 3, 0, 2, 0, 0, 0, 1, 2, 3}, []int{-1, 1, -1, 2, -1, 3, -1, 2, 1, 1, -1, -1, -1}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := avoidFlood(tt.rains)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
