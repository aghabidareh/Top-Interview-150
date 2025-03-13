class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        prev = [0] * (n + 1)
        for arr in triangle[::-1]:
            for i, v in enumerate(arr):
                prev[i] = v + (prev[i] if prev[i] < prev[i + 1] else prev[i + 1])

        return prev[0]