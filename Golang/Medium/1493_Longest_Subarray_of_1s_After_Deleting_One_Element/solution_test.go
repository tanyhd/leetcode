package longestsubarrayof1safterdeletingoneelement

import "testing"

func TestLongestSubarray(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		expected int
	}{
		{"Case 1", []int{1, 1, 0, 1}, 3},
		{"Case 2", []int{0, 1, 1, 1, 0, 1, 1, 0, 1}, 5},
		{"Case 3", []int{1, 1, 1}, 2},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := longestSubarray(tt.nums)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
