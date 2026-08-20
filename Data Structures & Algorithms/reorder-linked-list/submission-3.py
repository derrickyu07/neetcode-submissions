# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        second = prev
        first = head
        while second:
            node1 = first.next
            node2 = second.next
            first.next = second
            second.next = node1
            first = node1
            second = node2
        
