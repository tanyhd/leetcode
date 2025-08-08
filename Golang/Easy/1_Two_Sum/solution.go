package twosum

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)

	for i, num := range nums {
		complement := target - num
		if index, exist := numMap[complement]; exist {
			return []int{index, i}
		} else {
			numMap[num] = i
		}
	}
	return []int{}
}
