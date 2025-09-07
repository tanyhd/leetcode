package findnuniqueintegerssumuptozero

import "testing"

func TestSumZero(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected int
	}{
		{"Case 1", 5, 0},
		{"Case 2", 3, 0},
		{"Case 3", 1, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := sum(sumZero(tt.n))
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}

func sum(nums []int) int {
	count := 0
	for _, num := range nums {
		count += num
	}
	return count
}
