import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummyList = ListNode()
        answer = dummyList
        count = 0  # tiebreaker so Python never compares ListNodes

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, count, node))
                count += 1  # increment after every push

        while heap:
            val, _, popped_node = heapq.heappop(heap)  # unpack the tuple

            if popped_node.next:
                heapq.heappush(heap, (popped_node.next.val, count, popped_node.next))
                count += 1  # increment here too!

            answer.next = popped_node
            answer = answer.next

        return dummyList.next