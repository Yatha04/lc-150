class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxElements = []
        windowLen = 0
        left = 0
        right = 0

        for right in range(len(nums)):
            windowLen += 1
            maxNum = 0
            if (windowLen > k):
                left += 1
                windowLen -= 1
            if (windowLen == k):
                #print(windowLen)
                maxNum = float('-infinity')
                for i in range(left, right+1):
                    num = nums[i]
                    maxNum = max(num, maxNum)
                maxElements.append(maxNum)
        return maxElements

