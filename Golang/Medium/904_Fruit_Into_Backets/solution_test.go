package fruitintobackets

import "testing"

func TestTotalFruit(t *testing.T) {
	tests := []struct {
		name     string
		fruits   []int
		expected int
	}{
		{"Case 1", []int{1, 2, 1}, 3},
		{"Case 2", []int{0, 1, 2, 2}, 3},
		{"Case 3", []int{1, 2, 3, 2, 2}, 4},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := totalFruit(tt.fruits)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
