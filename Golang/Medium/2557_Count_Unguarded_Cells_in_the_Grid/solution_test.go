package countunguardedcellsinthegrid

import (
	"testing"
)

func TestCountUnguarded(t *testing.T) {
	tests := []struct {
		name     string
		m        int
		n        int
		guards   [][]int
		walls    [][]int
		expected int
	}{
		{"Case 1", 4, 6, [][]int{{0, 0}, {1, 1}, {2, 3}}, [][]int{{0, 1}, {2, 2}, {1, 4}}, 7},
		{"Case 2", 3, 3, [][]int{{1, 1}}, [][]int{{0, 1}, {1, 0}, {2, 1}, {1, 2}}, 4},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := countUnguarded(tt.m, tt.n, tt.guards, tt.walls)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
