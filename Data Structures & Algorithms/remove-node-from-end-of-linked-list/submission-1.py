# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp1 = head
        while tmp1:
            length += 1
            tmp1 = tmp1.next
        
        dummy = ListNode(0,head)
        target = length - n
        
        tmp2 = dummy

        for i in range(target):
            tmp2 = tmp2.next
        
        tmp2.next = tmp2.next.next

        return dummy.next