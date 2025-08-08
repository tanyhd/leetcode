package ransomnote

import "testing"

func TestMakeFancyString(t *testing.T) {
	tests := []struct {
		name       string
		ransomNote string
		magazine   string
		expected   bool
	}{
		{"Case 1", "a", "b", false},
		{"Case 2", "aa", "ab", false},
		{"Case 3", "aa", "aab", true},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := canConstruct(tt.ransomNote, tt.magazine)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
