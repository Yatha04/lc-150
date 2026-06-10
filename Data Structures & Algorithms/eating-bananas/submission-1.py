import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinishNanas(arr, k, hours):
            total = 0
            for i in arr:
                total += math.ceil(i/k)
            return (total <= hours)
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right )// 2

            if canFinishNanas(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left
