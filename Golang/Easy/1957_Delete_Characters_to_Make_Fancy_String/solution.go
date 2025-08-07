package deletecharacterstomakefancystring

import "strings"

func makeFancyString(s string) string {
	output := []string{}
	output = append(output, string(s[0]))
	count := 1

	for i := 1; i < len(s); i++ {
		c := string(s[i])
		if string(output[len(output)-1]) != c {
			output = append(output, c)
			count = 1
		} else {
			if count >= 2 {
				continue
			} else {
				count += 1
				output = append(output, c)
			}
		}
	}

	return strings.Join(output, "")
}
