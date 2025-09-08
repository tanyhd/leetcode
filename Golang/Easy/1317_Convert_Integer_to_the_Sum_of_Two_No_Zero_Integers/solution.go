package convertintegertothesumoftwonozerointegers

func getNoZeroIntegers(n int) []int {
	for i := 1; i <= n; i++ {
		if checkZero(i) && checkZero(n-i) {
			return []int{i, n - i}
		}
	}
	return []int{}
}

func checkZero(num int) bool {
	for num > 9 {
		if num%10 == 0 {
			return false
		}
		num = num / 10
	}
	return true
}
