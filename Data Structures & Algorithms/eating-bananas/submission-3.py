class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinish(speed, array, numHours):
            hours = 0
            for i in array:
                hours += (i // speed)
                if i%speed != 0:
                    hours += 1
            if hours <= numHours:
                return True
            else:
                return False
        
        left = 1
        right = max(piles)

        while left < right:

            mid = (left + right) // 2

            if canFinish(mid, piles, h):
                right = mid
            else:
                left = mid + 1
        return left