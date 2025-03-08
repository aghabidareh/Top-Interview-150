class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        all_of_strings = set(zip(s,t))
        set_of_s = set(s)
        set_of_t = set(t)
        return len(all_of_strings) == len(set_of_s) == len(set_of_t)