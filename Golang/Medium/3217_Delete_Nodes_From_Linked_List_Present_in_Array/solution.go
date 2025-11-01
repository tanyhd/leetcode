package deletenodesfromlinkedlistpresentinarray

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func modifiedList(nums []int, head *ListNode) *ListNode {
	numMap := make(map[int]int)

	for _, num := range nums {
		numMap[num] += 1
	}

	dummyHead := ListNode{0, nil}
	dummyHead.Next = head
	prev := &dummyHead
	current := dummyHead.Next

	for current != nil {
		if _, exist := numMap[current.Val]; exist {
			prev.Next = current.Next
			current = current.Next
			continue
		}

		prev = current
		current = current.Next
	}
	return dummyHead.Next
}
