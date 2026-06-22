# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = l1
        two = l2
        result = ListNode(0)
        ans = result
        carry = 0
        while one and two:
            sum = one.val + two.val
            sum += carry
            ans.next = ListNode(sum % 10)
            carry = 0
            carry = sum // 10
            one = one.next
            two = two.next
            ans = ans.next
        while one:
            sum = one.val + carry
            ans.next = ListNode(sum % 10)  # Changed from ans = ListNode(...) to keep the chain!
            carry = sum // 10
            one = one.next
            ans = ans.next
            
        # 3. If 'two' still has nodes, process them WITH the carry
        while two:
            sum = two.val + carry
            ans.next = ListNode(sum % 10)
            carry = sum // 10
            two = two.next
            ans = ans.next
            
        # 4. THE FINISH LINE: If both lists are empty but we still have a carry!
        if carry > 0:
            ans.next = ListNode(carry)
        
        return result.next