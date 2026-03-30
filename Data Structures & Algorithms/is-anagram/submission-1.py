class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = "".join(sorted(s, key=str.lower))
        t_sort = "".join(sorted(t, key=str.lower))
        return s_sort == t_sort

        