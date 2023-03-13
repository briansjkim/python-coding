import re

# Using package, space complexity not constant
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s)

        left, right = 0, len(new_str) - 1

        while left < right:
            if new_str[left].lower() != new_str[right].lower():
                return False
            left += 1
            right -= 1
        return True


# No package use, space complexity is constant

# valid palindrome if it reads the same forwards and backwards (two pointers - 1 at the start, 1 at the end)
#     all uppercase letters into lowercase letters => check only for lowercase (convert all characters to lowercase)
#     remove all non-alphanumeric characters (only check for characters between these ranges A-Z, a-z, 0-9)
#         check if the current character at both indices is an alphanumeric character
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.isAlphanumeric(s[left]):
                left += 1
            while right > left and not self.isAlphanumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isAlphanumeric(self, c: str) -> bool:
#         is the current character an alphanumeric character?
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

