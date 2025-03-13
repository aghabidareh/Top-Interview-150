class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s2), len(s1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        if s3[0] == s1[0]:
            dp[0][1] = 1
        if s3[0] == s2[0]:
            dp[1][0] = 1
        for i in range(m + 1):
            for j in range(n + 1):
                if j > 0:
                    if dp[i][j - 1] != 0 and s3[i + j - 1] == s1[j - 1]:
                        dp[i][j] = i + j
                if i > 0:
                    if dp[i - 1][j] != 0 and s3[i + j - 1] == s2[i - 1]:
                        dp[i][j] = i + j
        return dp[i][j] == m + n