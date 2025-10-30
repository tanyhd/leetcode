package minimumnumberofincrementsonsubarraystoformatargetarray

import "testing"

func TestMinNumberOperations(t *testing.T) {
	tests := []struct {
		name     string
		target   []int
		expected int
	}{
		{"Case 1", []int{1, 2, 3, 2, 1}, 3},
		{"Case 2", []int{3, 1, 1, 2}, 4},
		{"Case 3", []int{3, 1, 5, 4, 2}, 7},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := minNumberOperations(tt.target)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
