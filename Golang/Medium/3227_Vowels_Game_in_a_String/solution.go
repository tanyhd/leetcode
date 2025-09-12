package vowelsgameinastring

func doesAliceWin(s string) bool {
	vowels := map[rune]bool{
		'a': true,
		'e': true,
		'i': true,
		'o': true,
		'u': true,
	}

	for _, c := range s {
		if _, exist := vowels[c]; exist {
			return true
		}
	}
	return false
}
