package maximumnumberofwordsyoucantype

import "testing"

func TestCanBeTypedWords(t *testing.T) {
	tests := []struct {
		name          string
		text          string
		brokenLetters string
		expected      int
	}{
		{"Case 1", "hello world", "ad", 1},
		{"Case 2", "leet code", "lt", 1},
		{"Case 3", "leet code", "e", 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			result := canBeTypedWords(tt.text, tt.brokenLetters)
			if result != tt.expected {
				t.Errorf("expected %v, got %v", tt.expected, result)
			}
		})
	}
}
