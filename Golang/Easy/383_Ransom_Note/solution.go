package ransomnote

func canConstruct(ransomNote string, magazine string) bool {
	magMap := make(map[string]int)

	for _, v := range magazine {
		magMap[string(v)] += 1
	}

	for _, v := range ransomNote {
		c := string(v)
		if _, exist := magMap[c]; !exist {
			return false
		}
		magMap[c] -= 1
		if magMap[c] < 0 {
			return false
		}
	}
	return true
}
