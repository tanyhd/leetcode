package rangeproductqueriesofpowers

import (
	"math"
	"strconv"
)

func productQueries(n int, queries [][]int) []int {
	bNum := strconv.FormatInt(int64(n), 2)

	powers := []int{}
	count := 0
	for i := len(bNum) - 1; i >= 0; i-- {
		num := string(bNum[i])
		if num == "1" {
			v := math.Pow(2.0, float64(count))
			powers = append(powers, int(v))
		}
		count += 1
	}

	const mod = 1000000007
	output := []int{}
	for _, q := range queries {
		v := 1
		start := q[0]
		stop := q[1]
		for i := start; i <= stop; i++ {
			v = (v * powers[i]) % mod
		}
		output = append(output, v)
	}
	return output
}
