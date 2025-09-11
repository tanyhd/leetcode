package sortvowelsinastring

import "sort"

func sortVowels(s string) string {
	vowels := map[rune]bool{
		'A': true, 'E': true, 'I': true, 'O': true, 'U': true,
		'a': true, 'e': true, 'i': true, 'o': true, 'u': true,
	}
	var toSort []rune

	for _, w := range s {
		if _, exist := vowels[w]; exist {
			toSort = append(toSort, w)
		}
	}

	sort.Slice(toSort, func(i, j int) bool {
		return toSort[i] < toSort[j]
	})

	p := 0
	output := make([]rune, 0, len(s))

	for _, w := range s {
		if _, exist := vowels[w]; exist {
			output = append(output, toSort[p])
			p += 1
		} else {
			output = append(output, w)
		}
	}
	return string(output)
}
