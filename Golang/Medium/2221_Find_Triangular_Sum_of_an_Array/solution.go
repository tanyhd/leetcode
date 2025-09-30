package findtriangularsumofanarray

func triangularSum(nums []int) int {
	for len(nums) > 1 {
		tempArray := []int{}
		for i := 0; i < len(nums)-1; i++ {
			tempArray = append(tempArray, (nums[i]+nums[i+1])%10)
		}
		nums = tempArray
	}
	return nums[0]
}
