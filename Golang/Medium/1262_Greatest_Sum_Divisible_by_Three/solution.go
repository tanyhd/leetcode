package greatestsumdivisiblebythree

import "math"

type state struct {
	p   int
	rem int
}

func maxSumDivThree(nums []int) int {
	return helper(nums, 0, 0, make(map[state]int))
}

func helper(nums []int, p int, rem int, memo map[state]int) int {
	key := state{p, rem}
	if v, exist := memo[key]; exist {
		return v
	}

	if p == len(nums) {
		if rem == 0 {
			return 0
		}
		return int(math.Inf(-1))
	}

	pick := nums[p] + helper(nums, p+1, (rem+nums[p])%3, memo)
	dunPick := helper(nums, p+1, rem, memo)
	memo[key] = max(pick, dunPick)
	return memo[key]
}
