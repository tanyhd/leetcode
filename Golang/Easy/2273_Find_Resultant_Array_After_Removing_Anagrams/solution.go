package findresultantarrayafterremovinganagrams

func removeAnagrams(words []string) []string {
	output := []string{words[0]}

	for i := 1; i < len(words); i++ {
		if isAnagram(output[len(output)-1], words[i]) {
			continue
		}
		output = append(output, words[i])
	}
	return output
}

func isAnagram(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}

	s1Map := make(map[rune]int)
	for _, w := range s1 {
		s1Map[w] += 1
	}

	for _, w := range s2 {
		if _, exist := s1Map[w]; !exist {
			return false
		}
		s1Map[w] -= 1
		if s1Map[w] == 0 {
			delete(s1Map, w)
		}
	}
	return len(s1Map) == 0
}
