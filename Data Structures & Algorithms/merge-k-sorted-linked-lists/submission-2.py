import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ListNode.__lt__ = lambda self, other : self.val < other.val

        heap = []
        answer = ListNode(0)
        dummyNode = answer

        for node in lists:
            if node:
                heapq.heappush(heap, node)
        
        while heap:
            smallest_node = heapq.heappop(heap)
            dummyNode.next = smallest_node

            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next) 

            dummyNode = dummyNode.next
        
        return answer.next
