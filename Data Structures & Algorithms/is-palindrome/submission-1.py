import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        left = 0
        right = len(cleaned_text) - 1

        while left <= right:
            if cleaned_text[left].lower() != cleaned_text[right].lower():
                return False
            left += 1
            right -= 1
        return True