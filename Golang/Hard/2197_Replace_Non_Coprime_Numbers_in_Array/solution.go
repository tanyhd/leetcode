package replacenoncoprimenumbersinarray

func replaceNonCoprimes(nums []int) []int {
	stack := []int{}
	for _, num := range nums {
		current := num
		for len(stack) != 0 && !isCoprime(stack[len(stack)-1], current) {
			index := len(stack) - 1
			lastNum := stack[index]
			stack = stack[:index]
			current = LCM(lastNum, current)
		}
		stack = append(stack, current)
	}
	return stack
}

func isCoprime(a int, b int) bool {
	return gcd(a, b) == 1
}

func LCM(a int, b int) int {
	g := gcd(a, b)
	return a / g * b
}

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
