class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                ch += i.lower()
        return True if ch == ch[::-1] else False
