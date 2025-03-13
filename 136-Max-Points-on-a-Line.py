class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = 0
        for p1 in points:
            slopes = dict()
            for p2 in points:
                if p1 == p2: continue
                m = (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else float('inf')
                if m not in slopes:
                    slopes[m] = 1
                else:
                   slopes[m] += 1
            n = max(n, 1+(max(slopes.values()) if slopes.values() else 0))
        return n