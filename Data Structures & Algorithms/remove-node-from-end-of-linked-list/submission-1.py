# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        # right = head + n
        for _ in range(n):
            right = right.next
        # Traversing the linked list
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next