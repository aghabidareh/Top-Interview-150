class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        result, current_start = 1, points[-1][0]
        for start,end in reversed(points):
            if end<current_start:
                current_start = start
                result += 1
        return result