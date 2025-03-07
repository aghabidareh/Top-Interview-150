class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        counter = 0
        for i in range(len(t)):
            if counter <= len(s)-1 and s[counter] == t[i]:
                counter += 1

        return counter == len(s)