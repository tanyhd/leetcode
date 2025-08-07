package deletecharacterstomakefancystring

import "testing"

func TestMakeFancyString(t *testing.T) {
	tests := []struct {
		name     string
		s        string
		expected string
	}{
		{"Case 1", "leeetcode", "leetcode"},
		{"Case 2", "aaabaaaa", "aabaa"},
		{"Case 3", "aab", "aab"},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := makeFancyString(tt.s)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
