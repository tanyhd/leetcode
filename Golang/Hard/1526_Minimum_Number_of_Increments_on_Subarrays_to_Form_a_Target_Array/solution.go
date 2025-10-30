package minimumnumberofincrementsonsubarraystoformatargetarray

func minNumberOperations(target []int) int {
	count := target[0]

	for i := 0; i < len(target)-1; i++ {
		if target[i] < target[i+1] {
			count += target[i+1] - target[i]
		}
	}
	return count
}
