class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()

        if len(s) != len(t):
            return False
        from collections import Counter
        return Counter(s) == Counter(t)