# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        numSet = set()
        for i in range(len(nums)):
            numSet.add(nums[i])

        dummyHead = ListNode(0)
        dummyHead.next = head
        prev = dummyHead
        current = dummyHead.next

        while current != None:
            if current.val in numSet:
                prev.next = current.next
                current = current.next
                continue

            prev = current
            current = current.next
        
        return dummyHead.next