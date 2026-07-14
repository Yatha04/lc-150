# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #split the linked list
        #reverse the 2nd half
        #insert elements into new linked list one by one
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None
        
        #Reverse the second half
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        ans = ListNode(0)

        one = first
        two = second
        while two:
            tmp1 = one.next
            tmp2 = two.next
            one.next = two
            two.next = tmp1
            one = tmp1
            two = tmp2
            
