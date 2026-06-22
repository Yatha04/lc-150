# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        #got the middle element
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #print (slow.val,  fast.val if fast else None)
        #split it into 2 Linked Lists
        second = slow.next
        slow.next = None

        #reorder the second list
        prev = None
        curr = second

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        second = prev

        #merge head & second one by one:
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            first.next.next = tmp1

            first = tmp1
            second = tmp2
        return None



