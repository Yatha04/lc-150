# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # --- PASS 1: Count length ---
        original = head
        length = 0
        while head:
            length += 1
            head = head.next
            
        target = length - n
        
        # --- PASS 2: Traverse and Delete ---
        dummy = ListNode(0)
        dummy.next = original
        
        curr = dummy # Use a separate pointer to walk!
        
        # Take exactly 'target' steps forward
        for _ in range(target):
            curr = curr.next
            
        # curr is now standing exactly one node BEFORE the one we want to delete.
        # Drop the hammer and bypass the target node:
        curr.next = curr.next.next
        
        # Return the actual head of the list (which is whatever comes right after dummy)
        return dummy.next