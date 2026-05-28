class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLen = 0

        seen = set()
        left = 0
        right = 0
        count = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            count = right - left + 1
            longestLen = max(count, longestLen)
            print(seen)

        return longestLen