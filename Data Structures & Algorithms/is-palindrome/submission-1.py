class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([i for i in s if i.isalnum()]).lower()
        rev_s = "".join(list(s)[::-1])
        return True if s == rev_s else False