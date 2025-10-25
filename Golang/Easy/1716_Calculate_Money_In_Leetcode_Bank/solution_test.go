package calculatemoneyinleetcodebank

import "testing"

func TestTotalMoney(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		expected int
	}{
		{"Case 1", 4, 10},
		{"Case 2", 10, 37},
		{"Case 3", 20, 96},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := totalMoney(tt.n)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
