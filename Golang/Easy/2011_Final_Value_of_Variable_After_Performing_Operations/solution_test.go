package finalvalueofvariableafterperformingoperations

import "testing"

func TestFinalValueAfterOperations(t *testing.T) {
	tests := []struct {
		name       string
		operations []string
		expected   int
	}{
		{"Case 1", []string{"--X", "X++", "X++"}, 1},
		{"Case 2", []string{"++X", "++X", "X++"}, 3},
		{"Case 3", []string{"X++", "++X", "--X", "X--"}, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := finalValueAfterOperations(tt.operations)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
