package numberofpeopleawareofasecret

import (
	"testing"
)

func TestPeopleAwareOfSecret(t *testing.T) {
	tests := []struct {
		name     string
		n        int
		delay    int
		forget   int
		expected int
	}{
		{"Case 1", 6, 2, 4, 5},
		{"Case 2", 4, 1, 3, 6},
		{"Case 3", 4, 1, 4, 8},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := peopleAwareOfSecret(tt.n, tt.delay, tt.forget)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
