class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        left = 0
        right = 0

        for right in range(len(s2)):

            if (right - left + 1) > len(s1):
                left += 1
            newStr = sorted(s2[left:right+1])
            if newStr == s1:
                return True
        return False