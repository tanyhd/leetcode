package numberofpeopleawareofasecret

type state struct {
	start      int
	currentDay int
}

func peopleAwareOfSecret(n int, delay int, forget int) int {
	return person(1, 1, n, delay, forget, make(map[state]int))
}

func person(start int, currentDay int, n int, delay int, forget int, memo map[state]int) int {
	const mod = 1_000_000_007
	key := state{start, currentDay}
	if v, exist := memo[key]; exist {
		return v
	}

	if currentDay > n {
		if n-start < forget {
			return 1
		} else {
			return 0
		}
	}

	count := 0
	if start+delay <= currentDay && currentDay-start < forget {
		count += person(currentDay, currentDay+1, n, delay, forget, memo) % mod
	}

	count += person(start, currentDay+1, n, delay, forget, memo) % mod

	memo[key] = count
	return count
}
