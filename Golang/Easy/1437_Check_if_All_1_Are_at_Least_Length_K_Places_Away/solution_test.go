package checkifall1areatleastlengthkplacesaway

import "testing"

func TestNumWaterBottles(t *testing.T) {
	tests := []struct {
		name     string
		nums     []int
		k        int
		expected bool
	}{
		{"Case 1", []int{1, 0, 0, 0, 1, 0, 0, 1}, 2, true},
		{"Case 2", []int{1, 0, 0, 1, 0, 1}, 2, false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := kLengthApart(tt.nums, tt.k)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
