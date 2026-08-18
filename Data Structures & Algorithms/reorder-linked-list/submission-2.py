# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev
        while second:
            node1 = first.next
            node2 = second.next
            first.next = second
            second.next = node1
            first= node1
            second = node2

        