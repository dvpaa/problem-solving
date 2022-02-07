class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join([x.lower() for x in s if x.isalnum()])
        if a == a[::-1]:
            return True
        else:
            return False