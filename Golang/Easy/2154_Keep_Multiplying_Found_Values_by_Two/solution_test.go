package keepmultiplyingfoundvaluesbytwo

import "testing"

func TestFindFinalValue(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		original int
		expected int
	}{
		{"Case 1", []int{5, 3, 6, 1, 12}, 3, 24},
		{"Case 2", []int{2, 7, 9}, 4, 4},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := findFinalValue(tt.nums, tt.original)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
