class Solution:
    def isPalindrome(self, s: str) -> bool:
        # inspired from top on neetcode
        s = s.lower()
        s = list(filter(lambda x: x.isalnum(), s))
        return s == s[::-1]

        # My solution
        # s = "".join([i for i in s if i.isalnum()]).lower()
        # rev_s = "".join(list(s)[::-1])
        # return True if s == rev_s else False