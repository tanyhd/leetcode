package maximum69number

import "testing"

func TestMakeFancyString(t *testing.T) {
	tests := []struct {
		name     string
		num      int
		expected int
	}{
		{"Case 1", 9669, 9969},
		{"Case 2", 9996, 9999},
		{"Case 3", 9999, 9999},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := maximum69Number(tt.num)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
