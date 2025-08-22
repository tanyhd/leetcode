package largest3samedigitnumberinstring

import "testing"

func TestLargestGoodInteger(t *testing.T) {
	tests := []struct {
		name     string
		num      string
		expected string
	}{
		{"Case 1", "6777133339", "777"},
		{"Case 2", "2300019", "000"},
		{"Case 3", "42352338", ""},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := largestGoodInteger(tt.num)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
