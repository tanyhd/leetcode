package findxsumofallklongsubarraysi

import "sort"

func findXSum(nums []int, k int, x int) []int {
	output := []int{}
	p1 := 0
	p2 := k - 1

	for p2 < len(nums) {
		output = append(output, calculateSum(p1, p2, nums, x))
		p1 += 1
		p2 += 1
	}
	return output
}

func calculateSum(p1 int, p2 int, nums []int, x int) int {
	numMap := make(map[int]int)

	for i := p1; i <= p2; i++ {
		numMap[nums[i]] += 1
	}

	numArray := [][]int{}
	for num, count := range numMap {
		numArray = append(numArray, []int{count, num})
	}

	sort.Slice(numArray, func(i, j int) bool {
		if numArray[i][0] != numArray[j][0] {
			return numArray[i][0] > numArray[j][0]
		}

		if len(numArray[i]) > 1 && len(numArray[j]) > 1 {
			return numArray[i][1] > numArray[j][1]
		}
		return false
	})

	total := 0
	length := min(len(numArray), x)
	for i := 0; i < length; i++ {
		count := numArray[i][0]
		num := numArray[i][1]
		total += count * num
	}
	return total
}
