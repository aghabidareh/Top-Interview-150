class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        choices = sorted([(p, c) for p, c in zip(profits, capital)], key=lambda x: x[1])
        h = []

        idx = 0
        while idx < len(choices) and choices[idx][1] <= w:
            heapq.heappush(h, -choices[idx][0])
            idx += 1

        output = w
        for _ in range(k):
            if not h:
                return output
            output -= heapq.heappop(h)
            while idx < len(choices) and choices[idx][1] <= output:
                heapq.heappush(h, -choices[idx][0])
                idx += 1

        return output