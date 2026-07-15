# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.GetKth(groupPrev, k)
            if not kth : break

            groupNext = kth.next

            # reversing the current group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            #attach the reversed group to the rest of the list
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    
    def GetKth(self, curr, k):
        while k > 0 and curr:
            curr = curr.next
            k -= 1
        return curr