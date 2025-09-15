package maximumnumberofwordsyoucantype

import "strings"

func canBeTypedWords(text string, brokenLetters string) int {
	letterMap := make(map[rune]bool)

	for _, letter := range brokenLetters {
		letterMap[letter] = true
	}

	textArray := strings.Fields(text)

	count := 0
	for _, t := range textArray {
		for _, w := range t {
			if _, exist := letterMap[w]; exist {
				count -= 1
				break
			}
		}
		count += 1
	}
	return count
}
