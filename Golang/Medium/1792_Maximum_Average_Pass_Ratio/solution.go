package maximumaveragepassratio

import "container/heap"

type ClassStats struct {
	potentialIncrease float64
	passNum           float64
	total             float64
}

type ClassHeap []ClassStats

func (h ClassHeap) Len() int {
	return len(h)
}

func (h ClassHeap) Less(i, j int) bool {
	return h[i].potentialIncrease > h[j].potentialIncrease
}

func (h ClassHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *ClassHeap) Push(x any) {
	*h = append(*h, x.(ClassStats))
}

func (h *ClassHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxAverageRatio(classes [][]int, extraStudents int) float64 {
	h := &ClassHeap{}
	for _, v := range classes {
		passNum, total := float64(v[0]), float64(v[1])
		potentialIncrease := ((passNum + 1) / (total + 1)) - (passNum / total)
		heap.Push(h, ClassStats{potentialIncrease, passNum, total})
	}

	for range extraStudents {
		v := heap.Pop(h).(ClassStats)
		passNum, total := v.passNum, v.total
		passNum += 1
		total += 1
		potentialIncrease := ((passNum + 1) / (total + 1)) - (passNum / total)
		heap.Push(h, ClassStats{potentialIncrease, passNum, total})
	}

	count := float64(0)
	for _, v := range *h {
		count += v.passNum / v.total
	}
	return count / float64(h.Len())
}
