class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        length_of_set_of_pattern = len(set(pattern))
        length_of_set_of_s = len(set(s))
        length_of_set_of_all_strings = len(set(zip_longest(pattern , s)))

        return length_of_set_of_pattern == length_of_set_of_s == length_of_set_of_all_strings