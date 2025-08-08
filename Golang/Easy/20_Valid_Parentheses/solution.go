package validparentheses

func isValid(s string) bool {
	brackets := []string{}
	bracketMap := map[string]string{
		")": "(",
		"]": "[",
		"}": "{",
	}

	for _, v := range s {
		c := string(v)
		lastIndex := len(brackets) - 1
		if v, exist := bracketMap[c]; exist {
			if lastIndex < 0 {
				return false
			}
			check := brackets[lastIndex]
			brackets = brackets[:lastIndex]
			if check != v {
				return false
			}
		} else {
			brackets = append(brackets, c)
		}
	}

	if len(brackets) != 0 {
		return false
	}
	return true
}
