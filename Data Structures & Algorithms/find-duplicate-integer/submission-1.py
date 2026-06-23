class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Floyd's cycle detection
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #slow and fast meet at intersection

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                break
        return slow

        