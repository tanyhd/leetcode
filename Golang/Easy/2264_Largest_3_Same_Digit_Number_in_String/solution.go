package largest3samedigitnumberinstring

import "strconv"

func largestGoodInteger(num string) string {
	maxCount := -1
	for i := 1; i < len(num)-1; i++ {
		if num[i-1] == num[i] && num[i] == num[i+1] {
			n, _ := strconv.Atoi(string(num[i]))
			maxCount = max(maxCount, n)
		}
	}

	if maxCount == -1 {
		return ""
	}
	numString := strconv.Itoa(maxCount)
	return numString + numString + numString
}
