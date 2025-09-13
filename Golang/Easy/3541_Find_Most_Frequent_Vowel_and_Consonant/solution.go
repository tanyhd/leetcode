package findmostfrequentvowelandconsonant

func maxFreqSum(s string) int {
	vowels := map[rune]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
	}

	cMap := make(map[rune]int)
	maxVowel := 0
	maxConsonant := 0

	for _, c := range s {
		if _, exist := vowels[c]; exist {
			if _, exist := cMap[c]; !exist {
				cMap[c] = 0
			}
			cMap[c] += 1
			maxVowel = max(maxVowel, cMap[c])
		} else {
			if _, exist := cMap[c]; !exist {
				cMap[c] = 0
			}
			cMap[c] += 1
			maxConsonant = max(maxConsonant, cMap[c])
		}
	}

	return maxVowel + maxConsonant

}
