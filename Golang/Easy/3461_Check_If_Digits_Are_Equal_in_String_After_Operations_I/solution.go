package checkifdigitsareequalinstringafteroperationsi

import "strconv"

func hasSameDigits(s string) bool {
	current := s

	for len(current) > 2 {
		temp := ""
		for i := 0; i < len(current)-1; i++ {
			temp += strconv.Itoa((int(current[i]) + int(current[i+1])) % 10)
		}
		current = temp
	}
	return current[0] == current[1]
}
