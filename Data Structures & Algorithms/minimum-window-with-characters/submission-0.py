class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for i in t:
            need[i] = need.get(i,0) + 1
        need_int = len(need)

        left = 0
        right = 0
        have = 0
        window = {}
        ans = ''
        ans_len = float('infinity')

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1

            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_int:
                if (right - left + 1) < ans_len:
                    ans_len = right - left + 1
                    ans = s[left:right + 1]

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1
        return ans