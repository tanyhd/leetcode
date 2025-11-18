package bitand2bitcharacters

func isOneBitCharacter(bits []int) bool {
	return helper(0, bits)
}

func helper(p int, bits []int) bool {
	if p >= len(bits) {
		return false
	}

	if p == len(bits)-1 {
		return true
	}

	one := false
	two := false
	if bits[p] == 0 {
		one = helper(p+1, bits)
	} else if bits[p] == 1 {
		two = helper(p+2, bits)
	}
	return one || two
}
