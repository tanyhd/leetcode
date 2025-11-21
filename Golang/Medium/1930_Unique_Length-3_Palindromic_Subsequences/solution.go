package uniquelength3palindromicsubsequences

func countPalindromicSubsequence(s string) int {
	letterSet := make(map[rune]bool)
	letterMap := make(map[rune][]int)

	for i, c := range s {
		if _, exist := letterSet[c]; !exist {
			letterSet[c] = true
			letterMap[c] = append(letterMap[c], i)
		} else {
			letterMap[c] = append(letterMap[c], i)
		}
	}

	count := 0
	for c, _ := range letterSet {
		startIndex := letterMap[c][0]
		endIndex := letterMap[c][len(letterMap[c])-1]

		betweenSet := make(map[rune]bool)
		for i := startIndex + 1; i < endIndex; i++ {
			betweenSet[rune(s[i])] = true
		}
		count += len(betweenSet)
	}
	return count
}
