class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        if len(s) != len(t):
            result = False
        else:
            checked = []
            for i in s:
                if i not in checked:
                    checked.append(i)
                    if s.count(i) != t.count(i):
                        result = False
                        break

        return result