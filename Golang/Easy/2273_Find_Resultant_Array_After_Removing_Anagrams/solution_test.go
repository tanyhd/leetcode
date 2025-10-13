package findresultantarrayafterremovinganagrams

import (
	"slices"
	"testing"
)

func TestRemoveAnagrams(t *testing.T) {
	tests := []struct {
		name     string
		words    []string
		expected []string
	}{
		{"Case 1", []string{"abba", "baba", "bbaa", "cd", "cd"}, []string{"abba", "cd"}},
		{"Case 2", []string{"a", "b", "c", "d", "e"}, []string{"a", "b", "c", "d", "e"}},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := removeAnagrams(tt.words)
			if !slices.Equal(result, tt.expected) {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
