class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.lower()
        t = t.lower()

        if len(s) != len(t):
            return False
         
        det_arr = []
        from collections import Counter

        s_a = sorted(s)
        t_a = sorted(t)

        s_count = Counter(s_a)
        t_count = Counter(t_a)

        for k,j in s_count.items():
            if t_count[k] == j:
                det_arr.append(True)
            else:
                det_arr.append(False)
        if False in det_arr:
            return False
        return True